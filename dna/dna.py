import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) == 3):
        database = sys.argv[1]
        sequence = sys.argv[2]

    else:
        print("need name of CSV file and text file")

    # TODO: Read database file into a variable
    with open(database) as file:
        dna_database = csv.DictReader(file)



    # TODO: Read DNA sequence file into a variable
    dna_sequence = open(sequence, "r")
    reader = dna_sequence.read()

    # TODO: Find longest match of each STR in DNA sequence
    final_count_AGATC = longest_match(reader, "AGATC")
    # print(final_count_AGATC)

    final_count_AATG = longest_match(reader, "AATG")
    # print(final_count_AATG)

    final_count_TATC = longest_match(reader, "TATC")
    # print(final_count_TATC)

    """ Tried to implement my own searcher
    # AGATC searcher
    agatc_count = agatc_searcher(reader)
    print(agatc_count)

    #AATG searcher
    aatg_count = aatg_searcher(reader)
    print(aatg_count)

    #TATC searcher
    tatc_count = tatc_searcher(reader)
    print(tatc_count)
    """

    # TODO: Check database for matching profiles

    found = False

    with open(database) as file:
        dna_database = csv.DictReader(file)

        for row in dna_database:
            if (str(final_count_AGATC) == row['AGATC']) and (str(final_count_AATG) == row['AATG']) and (str(final_count_TATC) == row['TATC']):
                print(row['name'])
                found = True

    if found != True:
        print("No match")




def longest_match(sequence, subsequence):
    # Returns length of longest run of subsequence in sequence.

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run




# Trying to make my own searcher

def agatc_searcher(reader):

    counter = 0
    highest_row = 0

    for i in range(len(reader)):

        if (reader[i: i + 5] == 'AGATC'):
            counter += 1
            start = i + 5

            while True:
                if (reader[start: start + 5] == 'AGATC'):
                    counter += 1
                    start = start + 5

                elif (reader[start: start + 5] != 'AGATC'):
                    if (counter > highest_row):
                        highest_row = counter
                    counter = 0
                    break
    return(highest_row)


def aatg_searcher(reader):

    counter = 0
    highest_row = 0

    for i in range(len(reader)):

        if (reader[i: i + 4] == 'AATG'):
            counter += 1
            start = i + 5

            while True:
                if (reader[start: start + 4] == 'AATG'):
                    counter += 1
                    start = start + 5

                elif (reader[start: start + 4] != 'AATG'):
                    if (counter > highest_row):
                        highest_row = counter
                    counter = 0
                    break
    return(highest_row)


def tatc_searcher(reader):

    counter = 0
    highest_row = 0

    for i in range(len(reader)):

        if (reader[i: i + 4] == 'TATC'):
            counter += 1
            start = i + 5

            while True:
                if (reader[start: start + 4] == 'TATC'):
                    counter += 1
                    start = start + 5

                elif (reader[start: start + 4] != 'TATC'):
                    if (counter > highest_row):
                        highest_row = counter
                    counter = 0
                    break
    return(highest_row)


main()