import typing_extensions
from multi_modal_filtering_example.target_simulation.state_machine import State, StateMachine
from multi_modal_filtering_example.target_simulation.target_state import TargetState


def test_state_machine_should_call_current_state_on_exit_after_transition():
    class StateA(State):
        on_exit_was_called = False

        @typing_extensions.override
        @classmethod
        def on_enter(cls):
            return cls()

        @typing_extensions.override
        def on_exit(self):
            StateA.on_exit_was_called = True

        @typing_extensions.override
        def transition(self):
            return StateB

        @typing_extensions.override
        def apply_to_target_state(self, target_state):
            return target_state

    class StateB(State):
        on_exit_was_called = False

        @typing_extensions.override
        @classmethod
        def on_enter(cls):
            return cls()

        @typing_extensions.override
        def on_exit(self):
            StateB.on_exit_was_called = True

        @typing_extensions.override
        def transition(self):
            return None

        @typing_extensions.override
        def apply_to_target_state(self, target_state):
            return target_state

    state_machine = StateMachine(StateA)
    
    state_machine.apply_state_to_target_and_iterate_machine(TargetState())

    assert StateA.on_exit_was_called and not StateB.on_exit_was_called

def test_state_machine_should_call_current_state_update_target():
    class StateA(State):
        apply_to_target_state_was_called = False

        @typing_extensions.override
        @classmethod
        def on_enter(cls):
            return cls()

        @typing_extensions.override
        def on_exit(self):
            pass

        @typing_extensions.override
        def transition(self):
            return StateB

        @typing_extensions.override
        def apply_to_target_state(self, target_state):
            StateA.apply_to_target_state_was_called = True
            return target_state

    class StateB(State):
        apply_to_target_state_was_called = False

        @typing_extensions.override
        @classmethod
        def on_enter(cls):
            return cls()

        @typing_extensions.override
        def on_exit(self):
            pass

        @typing_extensions.override
        def transition(self):
            return None

        @typing_extensions.override
        def apply_to_target_state(self, target_state):
            StateB.apply_to_target_state_was_called = True
            return target_state

    state_machine = StateMachine(StateA)

    state_machine.apply_state_to_target_and_iterate_machine(TargetState())

    assert StateA.apply_to_target_state_was_called and not StateB.apply_to_target_state_was_called
