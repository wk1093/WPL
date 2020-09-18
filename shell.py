import WPL

def shell():
    try:
        while True:
            text = input('WPL> ')
            if text.strip() == "": continue
            result, error = WPL.run('<stdin>', text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
