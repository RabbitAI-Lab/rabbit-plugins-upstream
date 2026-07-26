## Description: <br>
Access Canvas LMS course data, assignments, grades, submissions, due dates, and course materials through the Canvas REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pranavkarthik10](https://clawhub.ai/user/pranavkarthik10) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Students, instructors, and support agents use this skill to retrieve Canvas course, assignment, grade, submission, file, announcement, discussion, and inbox data from an authenticated Canvas LMS instance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Canvas API token that can read educational records such as grades, submissions, messages, course files, and assignments. <br>
Mitigation: Use the token only with the intended Canvas account, keep it out of shared logs and committed .env files, and revoke it when it is no longer needed. <br>
Risk: A wrong CANVAS_URL could send authenticated requests to an unintended Canvas domain. <br>
Mitigation: Verify that CANVAS_URL is the institution's real Canvas domain before running API commands. <br>
Risk: Unnecessary queries may expose more student or course information than needed for the task. <br>
Mitigation: Limit requests to the specific courses, assignments, submissions, or files needed for the user's current workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pranavkarthik10/skills/canvas-lms) <br>
- [Publisher profile](https://clawhub.ai/user/pranavkarthik10) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and REST API endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CANVAS_URL and CANVAS_TOKEN supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
