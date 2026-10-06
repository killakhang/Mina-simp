# Mina Sim

A relationship/social interaction simulation and training research project.

## Goals
- Stateful simulated characters rather than one-shot chat personas
- Conversation and relationship-state tracking
- Realistic asynchronous messaging simulations
- Measure interaction signals such as rapport, pressure/neediness, trust, boundaries, conflict and disengagement
- Healthy characters can assert boundaries when interactions become toxic
- Character behavior can vary by configured personality/state
- Feedback/evaluation data can be reviewed and used to improve future policies
- Keep measurements and model decisions observable through logs

## Design principles
The simulator should not treat attraction or relationship outcomes as guaranteed. Characters have agency, preferences, boundaries and a realistic possibility of rejection or disengagement.

Scoring is an experimental model, not a claim that human relationships can be reduced to objective numbers.

## Planned modules
- character/persona state
- conversation/session state
- relationship state
- message timing
- signal scoring
- boundary/toxicity state
- evaluator/feedback loop
- audit/telemetry
- model-provider abstraction

This repository consolidates the Mina/Mini training-bot and relationship-simulation direction into one project.
