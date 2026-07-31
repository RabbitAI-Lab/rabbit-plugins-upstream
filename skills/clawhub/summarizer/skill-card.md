## Description: <br>
Summarizes and audits supplied documents, meetings, papers, threads, transcripts, data, code changes, and multi-source material while preserving claims, attribution, numbers, hedges, and material omissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to compress supplied source material into faithful summaries, recaps, TLDRs, abstracts, release notes, and audience-specific cuts. It is also used to check summaries for omissions, unsupported claims, changed numbers, lost hedges, and attribution errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically read and update persistent local memory, shared contacts, and project records across runs. <br>
Mitigation: Install it only when persistent local summarization records are desired, and review storage settings such as store_summaries before using it with sensitive material. <br>
Risk: Confidential source material may produce derived titles, dates, contacts, deadlines, or project decisions that are written to local Clawic data files. <br>
Mitigation: Use store_summaries: none or a similarly restrictive storage preference for confidential documents, and review the local Clawic data paths after sensitive runs. <br>
Risk: Summaries can mislead if they drop material context, change hedges, alter numbers, or omit attribution. <br>
Mitigation: Use the skill's faithfulness and coverage checks for higher-stakes summaries, and review any generated summary before relying on it for decisions. <br>


## Reference(s): <br>
- [ClawHub Summarizer Skill Page](https://clawhub.ai/ivangdavila/skills/summarizer) <br>
- [Clawic Summarizer Page](https://clawic.com/skills/summarizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown or plain text summaries, audits, recaps, action lists, omission notes, and local preference or memory records when configured.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local Clawic summarizer, contacts, and project files according to the user's storage preferences.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
