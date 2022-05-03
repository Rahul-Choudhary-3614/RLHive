from hive.replays.circular_replay import CircularReplayBuffer, SimpleReplayBuffer
from hive.replays.legal_moves_replay import LegalMovesBuffer
from hive.replays.ppo_replay import PPOReplayBuffer
from hive.replays.prioritized_replay import PrioritizedReplayBuffer
from hive.replays.replay_buffer import BaseReplayBuffer
from hive.utils.registry import registry

registry.register_all(
    BaseReplayBuffer,
    {
        "CircularReplayBuffer": CircularReplayBuffer,
        "SimpleReplayBuffer": SimpleReplayBuffer,
        "PrioritizedReplayBuffer": PrioritizedReplayBuffer,
        "LegalMovesBuffer": LegalMovesBuffer,
        "PPOReplayBuffer": PPOReplayBuffer,
    },
)

get_replay = getattr(registry, f"get_{BaseReplayBuffer.type_name()}")
