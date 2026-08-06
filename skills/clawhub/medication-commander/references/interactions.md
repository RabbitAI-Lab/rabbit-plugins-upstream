# Drug Interaction Database Reference

This document describes the built-in drug-drug interaction database used by `medication_commander.py`.

## Database Structure

Each interaction entry contains:

| Field | Description |
|---|---|
| `drug_a` | First drug name (generic) |
| `drug_b` | Second drug name (generic) |
| `severity` | `major`, `moderate`, or `minor` |
| `description` | What happens when these two drugs are combined |
| `recommendation` | Clinical recommendation |

## Monitored Interactions (30+ pairs)

### Major Severity

| Drug A | Drug B | Description |
|---|---|---|
| Warfarin | Aspirin | Significantly increased bleeding risk |
| Warfarin | Ibuprofen | Increased anticoagulant effect and GI bleeding |
| Warfarin | Amiodarone | Markedly increases warfarin levels |
| Warfarin | Fluconazole | Inhibits warfarin metabolism, bleeding risk |
| Warfarin | Sulfamethoxazole | Enhanced anticoagulant effect |
| Warfarin | Ciprofloxacin | Increased warfarin effect |
| Warfarin | Metronidazole | Potent inhibition of warfarin metabolism |
| Lisinopril | Spironolactone | Severe hyperkalemia risk |
| Enalapril | Potassium chloride | Hyperkalemia |
| Lisinopril | Potassium chloride | Hyperkalemia |
| Clonidine | Propranolol | Rebound hypertension if clonidine stopped |
| SSRI (Fluoxetine) | MAOI (Phenelzine) | Serotonin syndrome risk |
| Tramadol | Fluoxetine | Serotonin syndrome risk |
| Tramadol | MAOI | Serotonin syndrome and seizure risk |
| Hydrocodone | Alprazolam | Severe respiratory depression |
| Oxycodone | Lorazepam | Respiratory depression risk |
| Methotrexate | Trimethoprim | Increased methotrexate toxicity (bone marrow suppression) |
| Simvastatin | Amiodarone | High rhabdomyolysis risk |
| Simvastatin | Clarithromycin | Rhabdomyolysis risk |
| Digoxin | Amiodarone | Increased digoxin toxicity |
| Digoxin | Verapamil | Elevated digoxin levels |
| Theophylline | Ciprofloxacin | Theophylline toxicity |
| Lithium | Ibuprofen | Increased lithium levels (toxicity) |
| Lithium | Hydrochlorothiazide | Reduced lithium excretion, toxicity |

### Moderate Severity

| Drug A | Drug B | Description |
|---|---|---|
| Simvastatin | Diltiazem | Increased statin levels, myopathy risk |
| Metformin | Cimetidine | Decreased metformin clearance |
| Ramipril | Potassium-sparing diuretics | Hyperkalemia |
| Gabapentin | Hydrocodone | Increased CNS depression |
| Amlodipine | Simvastatin | Increased statin levels |
| Sertraline | Ibuprofen | Increased GI bleeding risk |
| Clopidogrel | Omeprazole | Reduced clopidogrel activation |
| Levothyroxine | Calcium carbonate | Decreased levothyroxine absorption |
| Levothyroxine | Iron sulfate | Decreased levothyroxine absorption |
| Tamsulosin | Tadalafil | Orthostatic hypotension |

### Minor Severity

| Drug A | Drug B | Description |
|---|---|---|
| Acetaminophen | Warfarin | Minor INR increase with chronic high-dose use |

## Severity Definitions

- **Major** — The interaction is clinically significant and potentially life-threatening. Avoid combination or require close monitoring and dose adjustment under medical supervision.
- **Moderate** — The interaction may cause deterioration in patient status. Monitor therapy, consider alternatives, or adjust doses.
- **Minor** — The interaction is unlikely to require intervention but should be noted.

## Important Notes

This database covers a **limited** set of common drug-drug interactions. It does **not** cover:
- Drug-allergy interactions
- Drug-disease contraindications
- Drug-food interactions (except where noted)
- Drug-laboratory test interference
- Herbal / supplement interactions

**Always verify with a pharmacist or drug interaction database for a complete check.**
