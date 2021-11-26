def initialize():
    '''
    Initializes the global variables needed for the simulation.
    '''

    # current number of hedons, current number of health points
    global cur_hedons, cur_health

    # latest activity, how long the latest activity took
    global last_activity, last_activity_duration

    # if the player loses interest 
    global bored_with_stars

    # the current star activity offered, duration between each star being offered stored in a list
    global cur_star_activity
    global star_duration

    # boolean to check if the person is tired
    global is_tired

    # if they call an activity multiple times in a row, this checks what the total amount of time has been for that specific activity
    global running_time, textbook_time, resting_time


    # checks if running_time has gone past 180 once before
    global past_180

    # initalizes all the global variables
    cur_hedons = 0
    cur_health = 0

    last_activity = None
    last_activity_duration = 0

    bored_with_stars = False

    cur_star_activity = False
    star_duration = []

    is_tired = False

    running_time = 0
    textbook_time = 0
    resting_time = 0

    past_180 = False


'''
The function returns True iff a star can be taken and used to get more hedons for an activity. A star can only be taken if the activity the star is offered for is the current activity, if no time has passed between the star being offered and the activity, and if the user has not lost interest.
'''
def star_can_be_taken(activity):
    global cur_star_activity, bored_with_stars

    if (cur_star_activity == activity) and (bored_with_stars == False):
        return True
    else:
        return False


def perform_activity(activity, duration):
    global cur_health, cur_hedons, cur_star_activity
    global last_activity, last_activity_duration
    global running_time, textbook_time, resting_time
    global star_duration, star_counter
    global is_tired
    global past_180

    # <---------- running ---------->
    if activity == "running" and duration > 0:
        # <---------- health ---------->
        # if under 180, multiplies by 3 for health
        if duration + running_time <= 180:
            cur_health += 3 * duration
            past_180 = False

        # if running activity has been called multiple times but did not go past 180mins previously, it needs to go up to 180 first
        # and then start doing *1 instead of *3 for health
        elif duration + running_time >= 180 and not past_180:
            cur_health += (180 - running_time) * 3
            cur_health += duration - (180 - running_time)
            past_180 = True

        # if the total time has already gone past 180, it knows to just *1 for health
        elif duration + running_time >= 180 and past_180:
            cur_health += duration

        # <---------- hedons ---------->
        # if the user is not tired
        if is_tired == False:

            # if a star has been offered for running
            if cur_star_activity == "running" and duration > 0:
                if duration > 10:
                    cur_hedons += 50
                    cur_hedons -= 2 * (duration - 10)
                else:
                    cur_hedons += 5 * duration

            # if there is no star offered for running or if the star offered is not for running
            else:
                if duration > 10:
                    cur_hedons += 20
                    cur_hedons -= 2 * (duration - 10)
                else:
                    cur_hedons += 2 * duration

        # if the user is tired
        else:

            # if a star has been offered for running
            if cur_star_activity == "running":
                if duration > 10:
                    cur_hedons += 10
                    cur_hedons -= 2 * (duration - 10)
                else:
                    cur_hedons += duration

            # if there is no star offered for running or if the star offered is not for running
            else:
                cur_hedons -= 2 * duration

        # set variables
        running_time += duration
        textbook_time = 0
        resting_time = 120
        is_tired = True

    # <---------- textbooks ---------->
    elif activity == "textbooks" and duration > 0:

        # <---------- health ---------->
        cur_health += 2 * duration

        # <---------- hedons ---------->
        # if the user is not tired
        if is_tired == False:

            # if a star has been offered for textbooks
            if cur_star_activity == "textbooks":
                if duration > 20:
                    cur_hedons += 50
                    cur_hedons -= (duration - 20)
                elif duration > 10:
                    cur_hedons += 40
                    cur_hedons += (duration - 10)
                else:
                    cur_hedons += 4 * duration

            # if there is no star offered for textbooks or if the star offered is not for textbooks
            else:
                if duration > 20:
                    cur_hedons += 20
                    cur_hedons -= (duration - 20)
                else:
                    cur_hedons += duration

        # if the user is tired
        else:

            # if a star has been offered for textbooks
            if cur_star_activity == "textbooks":
                if duration > 10:
                    cur_hedons += 10
                    cur_hedons -= 2 * (duration - 10)
                else:
                    cur_hedons += duration

            # if there is no star offered for textbooks or if the star offered is not for textbooks
            else:
                cur_hedons -= 2 * duration

        # set variables
        running_time = 0
        textbook_time += duration
        resting_time = 120
        is_tired = True

    # <---------- resting ---------->
    elif activity == "resting" and duration > 0:

        # set variables
        running_time = 0
        textbook_time = 0
        resting_time -= duration

        # if the player has rested for 2 hrs or longer they are no longer tired
        if resting_time <= 0:
            is_tired = False

    # if more than 2 hrs has passed, reset star_counter to 0
    if len(star_duration) > 0:
        star_duration[-1] += duration

    #set variables
    last_activity = activity
    last_activity_duration = duration
    cur_star_activity = False

'''
This function returns the number of hedons the user has after an activity has been performed.
'''
def get_cur_hedons():
    return cur_hedons

'''
This function returns the number of helath points the player has after an activity has been performed.
'''
def get_cur_health():
    return cur_health

'''
This function sets the cur_star_activity to the activity when the function is called. It also starts the star_duration timer if this is the first star offered within 2 hrs and adds 1 to the star_counter. If three stars have already been offered within 2 hrs, the user loses interest.
'''
def offer_star(activity):
    global cur_star_activity
    global star_duration, bored_with_stars

    if bored_with_stars == False:
        if len(star_duration) > 1 and sum(star_duration) < 120:
            bored_with_stars = True
            cur_star_activity = False
        else:
            star_duration.append(0)
            star_duration = star_duration[max(0, len(star_duration) - 2):]
            cur_star_activity = activity


'''
The function returns the activity (either "resting", "running", or "textbooks") which would give the most hedons if the person performed it for one minute at the current time.
'''
def most_fun_activity_minute():
    global is_tired
    global cur_star_activity

    # local variable for the number of hedons for each activity
    running = 0
    textbooks = 0
    resting = 0

    # if the user is not tired
    if is_tired == False:

        # if the current star activity offered is running
        if cur_star_activity == "running":
            running += 5

        # if the current star activity offered is textbooks
        elif cur_star_activity == "textbooks":
            textbooks += 4

        # if there is no current star activity offered or if the current star activity offered is resting
        else:
            running += 2
            textbooks += 1

    # if the user is tired
    else:

        # if the current star activity offered is running
        if cur_star_activity == "running":
            running += 1

        # if the current star activity offered is textbooks
        elif cur_star_activity == "textbooks":
            textbooks += 1

        # if there is no current star activity offered or if the current star activity offered is resting
        else:
            running -= 2
            textbooks -= 2

    # if the max value of running, textbooks, or resting is running --> running offers the most hedons in one minute
    if max(running, textbooks, resting) == running:
        return "running"

    # if the max value of running, textbooks, or resting is textbooks --> textbooks offers the most hedons in one minute
    elif max(running, textbooks, resting) == textbooks:
        return "textbooks"

    # if the max value of running, textbooks, or resting is resting --> resting offers the most hedons in one minute
    else:
        return "resting"


if __name__ == '__main__':
'''
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
'''