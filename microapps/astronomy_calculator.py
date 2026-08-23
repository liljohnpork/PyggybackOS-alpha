def astro_calculator():
    import time
    import astropy.units as u
    from astroquery.simbad import Simbad

    Star_parallaxes = {
        0.768: "Proxima Centauri",
        0.747: "Alpha Centauri A and B",
        0.546: "Barnard's Star",
        0.503: "Luhman 16",
        0.448: "WISE 0855-0714",
        0.415: "Wolf 359",
        0.00451: "Betelgeuse",
        0.00731: "Polaris",
        0.23178: "Van Maanen's Star",
        0.37921: "Sirius",
        0.13023: "Vega",
        0.00378: "Rigel"
    }

    while True:
        print("\n================================")
        print("Astronomy Calculator Menu")
        print("================================")
        print("1. Speed, Distance and Time")
        print("2. Local Star Distance Calculator")
        print("3. Physical Size Calculator")
        print("4. Unit Converter")
        print("5. Weight Calculator")
        print("6. LIVE Database Star Distance Lookup")
        print("7. Quit")
        print("--------------------------------")

        try:
            choice = int(input("Choose an option (1-7): "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue

        if choice == 1:
            print("\nDistance Calculator")
            print("-------------------")
            v = float(input("Enter speed (mph): "))
            d = float(input("Enter Distance (miles): "))
            print(f"{v:.2f} Mph")
            time.sleep(0.5)
            print(f"{d:.2f} Miles")
            time.sleep(0.5)

            t = (d * u.imperial.mile) / (v * u.imperial.mile / u.hour)

            print(f"Time: {t.to(u.minute):.0f}")
            print(f"Time: {t.to(u.hour):.2f}")
            print(f"Time: {t.to(u.day):.2f}")

            if v >= 60:
                print("Fast speed")
            else:
                print("Slow speed")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 2:
            print("\nStar Distance Calculator")
            print("-------------------------")
            p = float(input("Enter parallax (arcseconds): "))
            
            pc = (p * u.arcsec).to(u.pc, equivalencies=u.parallax())

            print(f"Distance: {pc:.2f}")
            print(f"Distance: {pc.to(u.kpc):.2f}")
            print(f"Distance: {pc.to(u.lightyear):.2f}")
            print(f"Distance: {pc.to(u.kilolightyear):.2f}")
            time.sleep(0.5)

            closest_parallax = min(Star_parallaxes.keys(), key=lambda x: abs(p - x))

            if abs(p - closest_parallax) < 0.001:
                name = Star_parallaxes[closest_parallax]
                print(f"This matches the target distance to: {name}")
            else:
                print("Unknown star or star system in local memory script registry.")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 3:
            print("\nPhysical Size Calculator")
            print("-----------------------")
            d = float(input("Enter the distance (metres): "))
            θ = float(input("Enter the angle (arcseconds): "))

            m = (d * u.m) * (θ * u.arcsec).to(u.rad).value

            print(f"Physical Width: {m:.2f}")
            print(f"Physical Width: {m.to(u.km):.2f}")
            print(f"Physical Width: {m.to(u.imperial.mile):.2f}")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 4:
            print("\nUnit Converter")
            print("--------------")
            units = {1: u.cm, 2: u.m, 3: u.km, 4: u.imperial.mile, 5: u.au}

            print("1. Centimetres\n2. Metres\n3. Kilometres\n4. Miles\n5. Astronomical Units")
            unit_choice = int(input("Pick a starting unit: "))
            unit_choice2 = int(input("Pick a final unit: "))
            value = float(input("Enter a value: "))

            answer = (value * units[unit_choice]).to(units[unit_choice2])
            print(f"\nResult: {value} {units[unit_choice].name} = {answer:.5f}")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 5:
            print("\nWeight Calculator")
            print("------------------")
            planets = {1: "Mercury", 2: "Venus", 3: "Earth", 4: "Mars", 5: "Jupiter", 6: "Saturn", 7: "Uranus", 8: "Neptune", 9: "Pluto"}
            gravity = {1: 0.38, 2: 0.91, 3: 1, 4: 0.38, 5: 2.53, 6: 1.07, 7: 0.89, 8: 1.14, 9: 0.06}
            
            weight = float(input("Your Earth weight (kg): "))
            print("1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune\n9. Pluto")
            planet = int(input("Choose planet number: "))
            
            new_weight = weight * gravity[planet]
            print(f"You would weigh {new_weight:.2f} kg on {planets[planet]}")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 6:
            print("\nLIVE Database Star Distance Lookup")
            print("----------------------------------")
            star_name = input("Enter any real star name (e.g., Sirius, Betelgeuse, Vega): ")
            print(f"Querying SIMBAD database for '{star_name}'...")
            
            Simbad.reset_votable_fields()
            Simbad.add_votable_fields('plx_value')
            
            try:
                result_table = Simbad.query_object(star_name)
                
                if result_table is not None:
                    col_name = None
                    if 'PLX_VALUE' in result_table.colnames:
                        col_name = 'PLX_VALUE'
                    elif 'plx_value' in result_table.colnames:
                        col_name = 'plx_value'
                    
                    if col_name and not result_table[col_name].mask:
                        live_p = float(result_table[col_name])
                        live_p_arcsec = (live_p * u.mas).to(u.arcsec).value
                        
                        if live_p_arcsec > 0:
                            print(f"\nSuccess! Telemetry found.")
                            print(f"Measured Parallax: {live_p_arcsec:.6f} arcseconds")
                            
                            live_pc = (live_p_arcsec * u.arcsec).to(u.pc, equivalencies=u.parallax())
                            
                            print(f"Calculated Distance: {live_pc:.2f}")
                            print(f"Calculated Distance: {live_pc.to(u.lightyear):.2f}")
                        else:
                            print("The star has a 0 or negative parallax in the database.")
                    else:
                        print("Error: The star exists, but it has no Parallax data recorded!")
                else:
                    print("Error: SIMBAD returned an empty table. Check your star spelling or internet connection.")
                    
            except Exception as error_msg:
                print(f"An unexpected programming error occurred: {error_msg}")

            print("\n----------------------------------")
            input("Press Enter to return to the main menu...")

        elif choice == 7:
            print("Exiting tool... Goodbye!")
            break
            
        else:
            print("Invalid menu choice. Please select numbers 1 through 7.")
