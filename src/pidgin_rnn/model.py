"""
The model for pidgin-rnn.

a sender (MLP encoder, then a GRU emitting discrete symbols via straight-through
Gumbel-softmax) and a receiver (a GRU that reads the message and scores candidate
objects).

forward() accepts return_cache=True and returns a dict of internal activations, and a
patch argument (or forward hooks) overwrites a named activation for interventions.
"""

# TODO: implement. See README.md for the plan.
