import typing


class State(object):
    """
    Yanked from starlette.datascructures

    An object that can be used to store arbitrary state.

    Used for `app.state`.
    """

    def __init__(self, state: typing.Dict = None):
        if state is None:
            state = {}
        super(State, self).__setattr__("_state", state)

    def __setattr__(self, key: typing.Any, value: typing.Any) -> None:
        self._state[key] = value

    def __getattr__(self, key: typing.Any) -> typing.Any:
        try:
            return self._state[key]
        except KeyError:
            message = "'{}' object has no attribute '{}'"
            raise AttributeError(message.format(self.__class__.__name__, key))

    def __delattr__(self, key: typing.Any) -> None:
        del self._state[key]
