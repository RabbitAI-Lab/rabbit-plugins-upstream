## Description: <br>
Generate word frequency statistics and word cloud from social media comments <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dkgee](https://clawhub.ai/user/dkgee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and operators use this skill to summarize social media comment topics by generating word-frequency statistics and a visual word cloud from JSON comment data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Comment data can contain sensitive or regulated user content. <br>
Mitigation: Use approved input datasets and store generated word-frequency and image outputs in controlled locations. <br>
Risk: The script writes fixed output filenames in the selected output directory. <br>
Mitigation: Run it in a dedicated output directory to avoid replacing existing word_freq.json or word_cloud.png files. <br>
Risk: Generated word clouds depend on installed Python packages and available font support. <br>
Mitigation: Install the documented dependencies and verify the output image, especially for Chinese text rendering. <br>


## Reference(s): <br>
- [Sample comments JSON](references/sample_comments.json) <br>
- [Stop words list](references/stop_words.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis] <br>
**Output Format:** [JSON file and PNG image] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes word_freq.json and word_cloud.png to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
