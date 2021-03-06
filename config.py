import random as rand

SHARD_IDS = [0, 1, 2]
VALIDATOR_NAMES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
VALIDATOR_WEIGHTS = {}
for v in VALIDATOR_NAMES:
    VALIDATOR_WEIGHTS[v] = rand.uniform(5, 25)

TTL_CONSTANT = 10

NUM_GEN_ALICE_BOB = 20

# Experiment parameters
NUM_PROPOSALS = 1000
NUM_WITHIN_SHARD_RECEIPTS_PER_PROPOSAL = 10
NUM_BETWEEN_SHARD_RECEIPTS_PER_PROPOSAL = 10
MEMPOOL_DRAIN_RATE = 1
REPORT_INTERVAL = 10
PAUSE_LENGTH = 0.01
