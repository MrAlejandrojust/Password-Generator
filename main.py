#


def main():
    bean_height = 100

    try:
        hours = input('Enter the number of hours: ')
        hours = int(hours)

        if hours < 0:
            print('Please enter a positive number')
            quit()
        else:
            for i in range(0, hours - 1):
                bean_height = bean_height * 1.5 + 30

            bean_height = bean_height / 100
            bean_height = "{0:.2f}".format(bean_height)

            print('After {} Hours, the beanstalk was {} meters tall!'.format(hours, bean_height))
    except ValueError:
        print('Please enter a valid number of Hours')
        main()


if __name__ == '__main__':
    main()
