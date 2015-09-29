import time

def main():
    letters = [
        """
   * *
 *     *
*       *
*       *
*       *
 *     *
   * *
                """,

                """
**
**
**
**
**
**
*********
*********
                    """,
                    """
****      **
** **     **
**  **    **
**   **   **
**    **  **
**     ** **
**      ****
                    """

                    ]

    count = 0
    while True:
        if count != 3:
            print(letters[count])
            count += 1
        else:
            count = 0
        time.sleep(1)





if __name__ == '__main__':
    main()