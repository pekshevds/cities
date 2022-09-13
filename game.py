import cities

if __name__ == "__main__":

    parser = cities.init_parser()
    args = parser.parse_args()

    if args.city:

        found_cities = cities.find_cities(args.city, cities=cities.CITIES)
        random_city = cities.get_random_city(found_cities)
        print(f"""--found cities:{found_cities}\n
                --total found cities:{len(found_cities)}\n
                --random city:{random_city}""")
