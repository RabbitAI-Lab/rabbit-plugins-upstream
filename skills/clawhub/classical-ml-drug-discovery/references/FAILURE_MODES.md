# Failure modes and required responses (loaded on demand)

Referenced from `SKILL.md`. Consult when a run hits one of these situations.

| Failure | Response |
|---|---|
| Too few compounds | Reduce claims, prefer simple models, repeated/grouped validation, seek data |
| Only actives available | Don't invent inactives; use ranking, one-class/domain methods, or get screened negatives |
| Conflicting replicates | Investigate assay/provenance; aggregate only with a documented rule |
| One scaffold dominates | Grouped split; report scaffold-specific performance; diversify acquisition |
| Split lacks a class | Change split seed/design without consulting test outcomes; record the rule |
| SVM too slow | Linear SVM, kernel approximation, smaller tuning set, or boosted trees |
| XGBoost unavailable | Run classical GB and document; don't rename it XGBoost |
| Strong CV, weak external test | Diagnose similarity/leakage/shift; don't tune against external labels |
| Poor calibration | Recalibrate on inner folds; report ranking and probability quality separately |
| Mostly OOD library | Acquire representative labels or restrict claims; don't force ranking as reliable |
| Importance changes by fold | Report instability; avoid mechanistic conclusions |
| Web predictor disagrees | Check endpoint/model/domain/version; don't average blindly |

