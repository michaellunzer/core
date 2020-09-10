"""Platform for sensor integration."""
from homeassistant.helpers.entity import Entity
from fortnite_python import Fortnite
from fortnite_python.domain import Platform
from fortnite_python.domain import Mode

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    ATTR_ATTRIBUTION,
    CONF_API_KEY,
    CONF_NAME,
    CONF_PLAYER,
    CONF_GAME_PLATFORM,
    CONF_MODE,
)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

REQUIREMENTS = ["fortnite-python==0.3.5"]

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Fortnite API Sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_PLAYER): cv.string,
        vol.Required(CONF_GAME_PLATFORM): cv.string,
        vol.Required(CONF_MODE): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""

    api_key = config.get(CONF_API_KEY)
    name = config.get(CONF_NAME)
    player = config.get(CONF_PLAYER)
    game_platform = config.get(CONF_GAME_PLATFORM)
    mode = config.get(CONF_MODE)

    # data = ShodanData(shodan.Shodan(api_key), query)

    fortnite = Fortnite(api_key)
    player = fortnite.player(player, Platform.game_platform)
    stats = player.get_stats(Mode.mode)
    data = stats.top1  # pylint: disable=maybe-no-member
    # hass.states.set("hello_fortnite.Hello_Fortnite", data)

    add_entities([FortniteSquadsWinsSensor(name, data)], True)


class FortniteSquadsWinsSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self.data = data
        self._name = "Fortnite Squads Wins"
        self._state = None
        self._unit_of_measurement = "Wins"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self.data.update()
        self._state = self.data


## This needs a lot of work and is not functioning!
##### based off of this:    https://github.com/home-assistant/core/blob/dev/homeassistant/components/shodan/sensor.py


class FortniteData:
    """Get the latest data and update the states."""

    def __init__(self, api, query):
        """Initialize the data object."""
        self._api = api
        self._query = query
        self.details = None

    def update(self):
        """Get the latest data from shodan.io."""
        # self.details = self._api.count(self._query)
        fortnite = Fortnite(api_key)
        player = fortnite.player(player, Platform.game_platform)
        stats = player.get_stats(Mode.mode)
        data = stats.top1  # pylint: disable=maybe-no-member
        # hass.states.set("hello_fortnite.Hello_Fortnite", data)
