## Description:

Amazon OpenSearch vector search expert knowledge base for vector search configuration, cluster tuning, quantization, cost optimization, instance sizing, pricing estimation, live cluster analysis, and benchmark planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[norrishuang](https://clawhub.ai/user/norrishuang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, size, tune, analyze, and benchmark Amazon OpenSearch vector search deployments. It supports guidance for k-NN configuration, quantization tradeoffs, cluster capacity planning, cost estimation, read-only live cluster analysis, and reproducible VectorDBBench experiment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cluster analyzer uses OpenSearch credentials and can print cluster and index metadata.

Mitigation: Use least-privilege read-only credentials where possible, keep secrets out of notes and generated artifacts, and review analysis output before sharing it.

Risk: Benchmark workflows can create, load, force-merge, or drop benchmark indices.

Mitigation: Run benchmarks only on disposable or dedicated benchmark clusters, inspect dry-run plans first, and require explicit confirmation before executing run commands.

Risk: OpenSearch network examples using 0.0.0.0 are unsafe if copied into production without controls.

Mitigation: Restrict production services to trusted private networks and enforce strong authentication, TLS, and firewall or security-group controls.

## Reference(s):

- [Vector Search and k-NN Optimization](references/vector-search.md)
- [OpenSearch 1-Bit Scalar Quantization (32x On-Disk)](references/quantization-1bit-32x.md)
- [OpenSearch Vector Quantization Techniques In-Depth](references/quantization-techniques.md)
- [OpenSearch Vector Search Cost Optimization Guide](references/cost-optimization.md)
- [Cluster Configuration and Tuning](references/cluster-tuning.md)
- [OpenSearch Vector Search Performance Benchmarks](references/performance-benchmarks.md)
- [Indexing Strategies and Best Practices](references/indexing-strategies.md)
- [Query Optimization Techniques](references/query-optimization.md)
- [OpenSearch Optimized Instances Guide](references/optimized-instances.md)
- [VectorDBBench Scenario Matrix](opensearch-vector-benchmark/references/scenario-matrix.md)
- [VectorDBBench Runbook](opensearch-vector-benchmark/references/runbook.md)
- [VectorDBBench Result Analysis](opensearch-vector-benchmark/references/result-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, YAML, and bash code blocks when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only cluster analysis JSON, AWS pricing query output, benchmark dry-run plans, and OpenSearch configuration examples.]

## Skill Version(s):

1.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
