## Description: <br>
Marktplaats-advertenties voorbereiden, plaatsen/bewerken, copy-QA, preflight, live-verificatie en register. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[roelbroersma](https://clawhub.ai/user/roelbroersma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents preparing normal Marktplaats sales listings use this skill to draft Dutch ad copy, choose categories, run copy and preflight gates, inspect the live form, verify saved ads, and update a local register. It is not intended for bulk posting, bypassing login or security challenges, or unattended paid options. <br>

### Deployment Geography for Use: <br>
Netherlands (Marktplaats.nl workflows) <br>

## Known Risks and Mitigations: <br>
Risk: Credentialed browser helpers or supplied credential options may be used against URLs outside the intended Marktplaats workflow. <br>
Mitigation: Review before installing, use only with a Marktplaats account and URLs the user controls, and avoid raw cookies, custom auth headers, or exported session data. <br>
Risk: Publishing or editing can affect real marketplace ads or paid promotion choices. <br>
Mitigation: Require explicit user approval for each publish, edit, paid option, or exception, and verify actions with copy-QA, preflight, browser probing, live verification, and register update gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/roelbroersma/skills/marktplaats-publisher) <br>
- [README](README.md) <br>
- [Marktplaats Seller Assistant - English Guide](references/guide-en.md) <br>
- [Marktplaats Verkoopassistent - Handleiding](references/handleiding-nl.md) <br>
- [Robust Posting Checklist](references/robust-posting-checklist.md) <br>
- [Setup voor kleine modellen](references/setup-small-model-nl.md) <br>
- [Rustige Safari en Background-Flow](references/background-safari-nl.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown listing copy, JSON ad records, and CLI PASS/FAIL output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or newer and a user-controlled Marktplaats browser session for authenticated publishing checks.] <br>

## Skill Version(s): <br>
0.6.3 (source: evidence.release.version, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
