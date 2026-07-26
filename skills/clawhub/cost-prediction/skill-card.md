## Description: <br>
Predict construction project costs using Machine Learning. Use Linear Regression, K-Nearest Neighbors, and Random Forest models on historical project data. Train, evaluate, and deploy cost prediction models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction estimators, analysts, and project teams use this skill to prepare historical project data, train cost prediction models, compare model performance, and generate cost forecasts with confidence ranges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses local filesystem access for user-selected datasets and trained model files. <br>
Mitigation: Review CSV input paths and model output locations before running generated code, and treat saved model files as local project artifacts. <br>
Risk: Generated construction cost predictions may be misleading when the training data is sparse, poor quality, or outside the new project's range. <br>
Mitigation: Use the skill's guidance to require adequate historical data, report confidence ranges, compare against benchmarks, and warn when extrapolating beyond training data. <br>
Risk: The manifest lists Linear Regression, K-Nearest Neighbors, and Random Forest while the artifact also includes a Gradient Boosting example. <br>
Mitigation: Confirm whether Gradient Boosting is part of the supported release before presenting it as a primary model option. <br>


## Reference(s): <br>
- [Cost Prediction Skill Page](https://clawhub.ai/datadrivenconstruction/skills/cost-prediction) <br>
- [datadrivenconstruction Publisher Profile](https://clawhub.ai/user/datadrivenconstruction) <br>
- [Data-Driven Construction](https://datadrivenconstruction.io) <br>
- [scikit-learn](https://scikit-learn.org) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with Python code blocks, metric tables, confidence ranges, feature importance rankings, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local file paths for datasets or saved model artifacts chosen by the user.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact/claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
