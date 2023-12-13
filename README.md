# LaunchDarkley
LaunchDarkly Excercise

I implemented the exercise using the Python SDK. I implemented a kill switch flag, a targeting flag based on Segment, and a multi-variant flag.

I am providing 2 python files to run, one for the user James and the other for Mary.

*** Setup Instructions for Launch Darkly ***

You will need to create 3 Feature Flags:

ApplicationAccess : 
        Type: Kill Switch
        Variations: Allow, Disabled
        Default Variation: Disabled
        Off Variation: Disabled
        Targeting : Individual Targets (James and Mary)

PowerUsers:
        Type: Custom
        Variations: Enabled, Disabled
        Default Variation: Disabled
        Off Variation: Disabled
        Targeting : Context is in Segment PowerUsers

Favorite Color:
        Type: Custom (String)
        Variations: Red, Yellow, Green
        Default Variation: Green
        Off Variation: Red
        Targeting: 

You will need to create 1 Segment Called PowerUsers
        Included Targets:  Mary

*** Setup Instructions for Python Files ***

You will need to have python installed on your local machine. 
Both files (James.py and Mary.py) will need to be modified at line 13 to replace the sdk value passed in:

        ldclient.set_config(Config("sdk-be592391-b88c-4fd6-874d-09e5b7a5e6c6"))  -> ldclient.set_config(Config("YOUR SDK KEY HERE"))

The first time you run Mary.py and James.py, a context for each will be created in LaunchDarkly. 
Please validate that the context keys are the same in LaunchDarkly as they are on line 24 of Mary.py and James.py

Once the contexts and the feature flags have been created, Set the values as follows:

    Mary - ApplicationAccess(Enabled), PowerUsers(Enabled), FavoriteColor(Yellow)
    James - ApplicationAccess(Enabled), PowerUsers(Disabled), FavoriteColor(Red)

Run the Pythonscripts for Mary and James. Notice the value of the feature flags
In LaunchDarkly, disable ApplicationAccess for James and run his python script
In LaunchDarkly, Change FavoriteColor for Mary to Red and run her python script

 
