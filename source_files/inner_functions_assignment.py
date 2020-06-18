def measurements(the_list):
    def area(a_list):
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        return 2 * a_list[0] + 2 * a_list[1]

    return "Perimeter = %s Area = %s" % (perimeter(the_list), area(the_list))

