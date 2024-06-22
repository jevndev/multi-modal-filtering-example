from __future__ import annotations

import abc
import typing

from multi_modal_filtering_example.target_simulation.target_state import TargetState


class State(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def on_enter(cls) -> typing.Self: ...

    @abc.abstractmethod
    def on_exit(self) -> None: ...

    @abc.abstractmethod
    def transition(self) -> typing.Type[State] | None: ...

    @abc.abstractmethod
    def apply_to_target_state(self, target_state: TargetState) -> TargetState: ...


class StateMachine:
    def __init__(self, initial_state: typing.Type[State]) -> None:
        self._current_state = initial_state.on_enter()

    def apply_state_to_target_and_iterate_machine(
        self, target_state: TargetState
    ) -> TargetState:
        new_target_state = self._current_state.apply_to_target_state(target_state)
        new_state_machine_state = self._current_state.transition()
        if new_state_machine_state is not None:
            self._current_state.on_exit()
            self._current_state = new_state_machine_state.on_enter()

        return new_target_state
