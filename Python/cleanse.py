#Website code for Cleanse
totalScore = 0
message15to19 = "YOU have Dry-Combination skin meaning you have excess oil being produced in certain areas of your face and dryness in other parts. You might experience oiliness specifically near your nose and forehead while the rest of your face might be dry. It's best for you to maintain hydration by moisturizing and combatting the excess oil by using proper cleansers. I'd suggest using the following in your routine: Ceramide-rich Moisturizers; Retinol, Sallicylic Acid and Hyaluronic Acid Cleansers, SPF Sunscreen, AHA & BHA Toners, Rice Toners; Vitamin C Serums; Niacinamide Moisturizing Gels and Serums."
message20to25 = "YOU have Combination-Oil skin meaning you have excess oil being produced all over your face. You might experience lots of acne and breakouts. It's best for you to maintain your skin barrier by moisturizing and combatting excess oil by using proper cleansers. I'd suggest using the following in your routine: Ceramide-rich Moisturizers; Retinol, Sallicylic Acid and Hyaluronic Acid Cleansers, SPF Sunscreen, AHA & BHA Toners, Rice Toners; Vitamin C Serums; Niacinamide Serums; Chemical exfoliants; Clay facemasks; Glycolic Acid Gels; Adapalene Gels." 
message10to14 = "YOU have Normal-Dry skin meaning your skin has either a balanced production of oil or less production in oil. You might experience dryness, flakiness, and tightness. It's best for you to maintain proper hydration by always moisturizing and not washing your face with harsh products too often. I'd suggest using the following in your routine: Vitamin E Oil; Ceramide-rich Moisturizers; Hyaluronic Acid Serums; Omega-3 Fatty-acids, Retinol, Gentle Cleansers, SPF Sunscreen, AHA & BHA Toners, Vitamin C Serums." 
deadSkinMessage = "Stop lying about your scoreeee" 
tryAgain = True

def introduceApplication():
        introMessage = "\nHi! My name is Raisa Ahsan and I created an application called CLEANSE to help you discover your skin type and products that will benefit you! You just have to answer the following questions honestly and you'll receive your results at the end.\n"
# print( "This applications helps you to ...." )
        print( introMessage )

#Retrieve questions list
questions = [
    'Do you have patchy or peely skin? Answer in "1" or "0"',
    'Do you have an oily or sweaty tzone? Answer in "1" or "0"',
    'Do you have sensitive skin? Answer in "1" or "0"',
    'Do you have deep lines or crinkles on your face? Answer in "1" or "0"',
    'Does your skin bleed sometimes? Answer in "1" or "0"',
    'Do you have lots of texture on your skin? Answer in "1" or "0"',
    'Do you have blackheads, little black dots that clog your pores? Answer in "1" or "0"',
    'Does your face become red often? Answer in "1" or "0"',
    'Is your skin rough? Answer in "1" or "0"',
    'Is the entirety of your face usually oily? Answer in "1" or "0"',
    'Do you have an oily tzone and oily cheeks? Answer in "1" or "0"',
    'Do you have large pores? Answer in "1" or "0"',
    'Do you have lots of acne? Answer in "1" or "0"',
    'Do you have more pores around your nose? Answer in "1" or "0"',
    'Does your face apppear shiny? Answer in "1" or "0"',
    'Does the skin around your face feel tight? Answer in "1" or "0"',
    'Do you suffer from inflammation? Answer in "1" or "0"',
    'Do you have whiteheads, little white dots that clog your pores? Answer in "1" or "0"',
    'Do you have a lot of closed comedones and small bumps on your face? Answer in "1" or "0"',
    'Do you suffer from reoccuring pimples? Answer in "1" or "0"',
    'Do you have clogged pores? Answer in "1" or "0"',
    'Do you often suffer from breakouts near your hairline? Answer in "1" or "0"',

]



while tryAgain:
    #start
    userResponse = input( "Type in start to start the application!: " )

    while userResponse.lower() != "start":
        userResponse = input( "Buddy :( I said to type in start to start the application: " )

    #intro
    introduceApplication()

    for currentQuestion in questions:
        userScoreAsAString = input( currentQuestion + ": " )
        userScoreAsANumber = int( userScoreAsAString )

        totalScore = totalScore + userScoreAsANumber

    #Add 3 to the total score
    totalScore = totalScore + 3

    # 10 to 14
    # 15 to 19
    # 20 to 25

    if totalScore < 10:
        print( deadSkinMessage )
    elif totalScore < 15:
        print( message10to14 )
    elif totalScore < 20:
        print( message15to19 )
    elif totalScore < 26:
        print( message20to25 )
    else:
        print( deadSkinMessage )


    print( f"Your total is {totalScore}" )

#if you want to try again
    userResponse = input( "Do you want to try again: y/n? ")
    if userResponse.lower() == "n":
        tryAgain = False

#End