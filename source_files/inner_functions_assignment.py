def measurements(the_list):
    if len(the_list) == 2:
        def area(a_list):
            return a_list[0] * a_list[1]

        def perimeter(a_list):
            return 2 * a_list[0] + 2 * a_list[1]

        return "Perimeter = %s Area = %s" % (perimeter(the_list), area(the_list))
    elif len(the_list) == 1:
        def area(a_list):
            return a_list[0] ** 2

        def perimeter(a_list):
            return a_list[0] * 4

        return "Perimeter = %s Area = %s" % (perimeter(the_list), area(the_list))
