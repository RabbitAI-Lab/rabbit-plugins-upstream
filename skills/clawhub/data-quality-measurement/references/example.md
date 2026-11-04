# Worked example: sampling two cohorts

Synthetic data. Population: 800 clinicians in A and 200 in B. Independently sample 8 from each cohort. All 8 A records are correct; 4 of 8 B records are correct.

The unweighted sample rate is 12/16 = 75%. It overrepresents the smaller cohort. With these known stratum sizes and representative samples within each stratum, the estimated population correctness is 0.8 × 1.0 + 0.2 × 0.5 = 90%.

B still has a serious observed problem: 4/8 records are wrong. Whether the delivery is usable depends on the intended customer population and consequences; the overall estimate does not settle that decision.

In a separate classification sample with 9 true positives, 1 false positive and 3 misses, precision is 9/10 = 90%; recall is 9/12 = 75%. If missed positives have not been measured, recall is unknown.

A separate simple random sample with no defects in 10 independent observations does not prove perfection. A 95% Wilson interval has an upper defect limit of about 27.8%. This is an illustrative confidence level, not an acceptance threshold.
