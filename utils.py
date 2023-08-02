from Consts import Match_Cond


def inputs_from_user():
    number_of_packs = None
    while type(number_of_packs) != int:
        try:
            number_of_packs = int(input('Please enter the number of packs to use for the game (between 1 and 4): ').strip())
        except ValueError:
            print('Please provide a number')

    matching_condition = None
    while matching_condition not in Match_Cond:
        if matching_condition is not None:
            print ('Incorrect Matching Condition')

        matching_condition = input('''
        Please choose a matching condition from one of these
        : {matching_conditions}
        '''.format(matching_conditions = list(Match_Cond.keys())))

    return number_of_packs, matching_condition