"""The hello_fortnite integration."""

# """Platform for sensor integration."""
from fortnite_python import Fortnite
from fortnite_python.domain import Platform
from fortnite_python.domain import Mode

REQUIREMENTS = ["fortnite-python==0.3.5"]

# The domain of your component. Equal to the filename of your component.
DOMAIN = "hello_fortnite"


def setup(hass, config):
    """Setup the hello_fortnite component."""
    # States are in the format DOMAIN.OBJECT_ID.
    fortnite = Fortnite("ea1b5a95-662b-4fce-be79-eb7f46344e55")
    player = fortnite.player("Captain_Crunch88", Platform.GAMEPAD)
    stats = player.get_stats(Mode.SQUAD)
    data = stats.top3  # pylint: disable=maybe-no-member
    hass.states.set("hello_fortnite.Hello_Fortnite", data)

    # Return boolean to indicate that initialization was successfully.
    return True
