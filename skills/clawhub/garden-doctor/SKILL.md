---
name: garden-doctor
description: Diagnoses plant problems from symptoms (yellow leaves, brown spots, drooping, pests). Provides likely diagnoses with confidence scores, treatment plans, and prevention tips using a knowledge base of 40+ common plant problems.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - gardening
  - plants
  - diagnosis
  - agriculture
  - troubleshooting
---

# Garden Doctor

An agent skill that diagnoses common plant health problems from reported symptoms and provides treatment plans.

## What It Does

- **Symptom-based diagnosis** — takes a plant type and list of symptoms, matches against a knowledge base of 40+ common problems.
- **Confidence scoring** — ranks each candidate diagnosis by how many reported symptoms it matches.
- **Treatment plans** — provides step-by-step treatment instructions for each diagnosis.
- **Prevention tips** — suggests long-term care changes to prevent recurrence.
- **Pest identification** — recognizes common pests (aphids, spider mites, fungus gnats, etc.) and their damage patterns.

## Quick Start

```bash
# Diagnose from symptoms
python3 scripts/garden_doctor.py diagnose \
  --plant "tomato" \
  --symptoms "yellow leaves" "brown spots on leaves" "drooping"

# List all known problems
python3 scripts/garden_doctor.py list

# Show details of a specific problem
python3 scripts/garden_doctor.py info --id overwatering

# Search by symptom keyword
python3 scripts/garden_doctor.py search --symptom "yellow leaves"
```

## Input Format

```bash
python3 scripts/garden_doctor.py diagnose \
  --plant "monstera" \
  --symptoms "yellow leaves" "brown spots" "wilting"
```

Symptoms are matched as keywords — partial matches work (e.g., "yellow" matches "yellow leaves", "yellowing lower leaves").

## Output

Diagnosis produces structured JSON:

```json
{
  "plant": "monstera",
  "symptoms_reported": ["yellow leaves", "brown spots", "wilting"],
  "diagnoses": [
    {
      "id": "root_rot",
      "name": "Root Rot (Overwatering)",
      "confidence": 0.85,
      "matched_symptoms": 3,
      "cause": "Soil stays soggy; roots suffocate and decay.",
      "treatment": [...],
      "prevention": [...]
    }
  ],
  "disclaimer": "This tool is for informational purposes..."
}
```

## Reference Documentation

- [`references/knowledge-base.md`](references/knowledge-base.md) — full catalog of 40+ plant problems
- [`references/symptoms-guide.md`](references/symptoms-guide.md) — symptom-to-cause reference

## Disclaimer

This tool is for informational and educational purposes only. For valuable or rare plants, consult a local horticulturist or agricultural extension service.
