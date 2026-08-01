## Description: <br>
Helps users plan practical local AI and LLM workflows on consumer CPU or family GPU hardware without relying on cloud-only systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, privacy-conscious users, hobbyists, and small teams use this skill to choose local LLM setup steps, constraints, checklists, and validation notes for ordinary home machines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to be invoked for loosely related local-AI or privacy requests. <br>
Mitigation: Review the user's actual goal and constraints before relying on the skill's guidance, and narrow the requested output when the request is ambiguous. <br>
Risk: Advisory setup guidance can become inaccurate as local LLM tools, model formats, and hardware support change. <br>
Mitigation: Verify proposed commands, hardware assumptions, and model compatibility against the current tool documentation before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/local-llm-setup-advisor-233439) <br>
- [Ask HN: MacBook vs. Dedicated GPU for LLM](https://news.ycombinator.com/item?id=48696532) <br>
- [SegmentFault: vLLM Disaggregated Prefill Lmcache](https://segmentfault.com/a/1190000046720505) <br>
- [SegmentFault: vLLM Disaggregated Prefill](https://segmentfault.com/a/1190000046807401) <br>
- [CSDN: LLM Intelligent Routing Hub](https://blog.csdn.net/weixin_32495691/article/details/162534869?ops_request_misc=elastic_search_misc&request_id=bc30966b6654401da509dbc1ab5b2228&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~ElasticSearch~search_v2-2-162534869-null-null.142^v102^control&utm_term=local%20LLM%20consumer%20GPU) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with optional inline code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tailored to the user's stated hardware, privacy needs, local-model constraints, and verification requirements when provided.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
