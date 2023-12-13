# Import the LaunchDarkly client.
import ldclient
from ldclient import Context
from ldclient.config import Config

# Create a helper function for rendering messages.
def show_message(s):
  print("*** %s" % s)
  print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-be592391-b88c-4fd6-874d-09e5b7a5e6c6"))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  show_message("SDK successfully initialized!")
else:
  show_message("SDK failed to initialize")
  exit()

# Set up the evaluation context. This context should appear on your LaunchDarkly contexts
# dashboard soon after you run the demo.
context = Context.builder('example-user-key2').name('Mary').build()

# Call LaunchDarkly with the feature flag key you want to evaluate.
flag_value = ldclient.get().variation("ApplicationAccess", context, False)

show_message("Feature flag 'ApplicationAccess' is %s for this User" % (flag_value))

if(flag_value):

  flag_value2 = ldclient.get().variation("PowerUsers", context, False)
  show_message("This user belongs to the PowerUser Segment: %s" % (flag_value2))

  flag_value3 = ldclient.get().variation("FavoriteColor", context, False)
  show_message("Favorite Color is: %s" % (flag_value3))

# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. If analytics events are not delivered,
# the user properties and flag usage statistics will not appear on your dashboard. In a
# normal long-running application, the SDK would continue running and events would be
# delivered automatically in the background.
ldclient.get().close()