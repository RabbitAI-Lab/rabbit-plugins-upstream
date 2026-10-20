# Structure prediction

## Goal and method

Predict structures for the user's molecular system and interpret the delivered confidence evidence. Prefer an applicable maintained multi-model prediction workflow over reconstructing its model combination independently. `Multi-Model Structure Prediction` identifies the intended workflow family, not a guaranteed platform identity or an instruction to run every available model.

## Inputs and choices

- Inspect supplied sequences or structures and their molecule types.
- Establish whether records represent independent prediction targets or chains in one complex. Preserve supplied pairing, chain labels, and stoichiometry; do not infer a biological assembly from file order.
- Resolve ligands, templates, or other modeling choices only when required for the intended system and supported by the chosen method. Do not invent them to make an input acceptable.

## Business workflow

1. Identify the intended prediction object and verify compatibility with the chosen workflow's supported molecules and chain organization.
2. Prepare the required sequence or structure inputs while preserving the user's system definition. Use documented defaults consistent with that objective.
3. Run the selected workflow and obtain its structures and confidence outputs. Reuse its declared model composition; add separate predictions only when requested or needed for an explicitly chosen comparison.
4. Match every output to its input target, chains, and prediction method. Report absent or failed products separately from completed predictions.

## Results

Deliver the available structures with their identities, method settings, and reported confidence measures. When comparing models, use documented metric meanings and equivalent molecular systems; do not invent a common score for incompatible metrics.

Distinguish prediction confidence and agreement between models from experimentally established structure quality. For existing-result requests, interpret the supplied evidence without starting a replacement prediction.
