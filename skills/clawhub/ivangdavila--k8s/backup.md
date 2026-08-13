# Backup and Restore — What Actually Comes Back

Before planning or claiming anything, read `## Due` and `deploys/<year>.md` in `~/Clawic/data/k8s/`: the only honest RTO is the one the last drill measured, and the only honest backup is one that has been restored. Production's three restore layers — cluster, manifests, data — set the order (`production.md`); this file is the mechanics of each one and the list of things that do not come back.

## What Each Tool Actually Captures

| Tool | Captures | Does not capture |
|---|---|---|
| GitOps repo | Every object you committed | Anything hand-applied: emergency Secrets, hotfixes, objects a controller created |
| Backup operator (Velero-class) | API objects, filtered by namespace/label, plus volume data via CSI snapshot or file-level copy | Anything the filter missed; the correctness of controller-owned status |
| CSI VolumeSnapshot | The block device at a point in time, crash-consistent | Application consistency — a half-written transaction is included (`storage.md`) |
| Database-native dump / PITR | A restorable database | Everything outside the database |
| etcd snapshot | Every API object in the cluster, including ones you deleted after the snapshot | The contents of any volume; not available at all on a managed control plane |
| Cloud disk snapshot | The disk | The PV/PVC objects that bind it to a pod — restoring the disk without the objects gives you data nothing mounts |

The rule that follows: **object backups and data backups are two different backups**, and a restore needs both, in that order. etcd snapshots restore the pods that mount empty disks; volume snapshots restore disks that nothing mounts.

## The Objects Nobody Backs Up

A namespace restore fails on these far more often than on volume data:

- **Hand-applied Secrets** — the TLS key someone created by hand, the pull secret, the API token. If `secrets_backend` is `plain` and they are not in Git, they exist only in etcd (`config-and-secrets.md`).
- **Cluster-scoped objects** the namespace depends on: CRDs, StorageClasses, PriorityClasses, ClusterRoles, IngressClasses, webhook configurations. A namespace-scoped backup omits every one of them, and the restore fails at admission or produces objects with no controller.
- **CRDs before their CRs.** Restoring a custom resource whose CRD does not exist yet fails; the ordering must be CRDs, then namespaces, then workloads, then jobs — the same ordering GitOps sync waves encode (`manifests.md`).
- **Controller-populated fields.** LoadBalancer IPs, cluster IPs, node names, `resourceVersion` and UIDs are all regenerated. A restore that tries to preserve them fails on immutable fields; one that drops them changes every external reference — a new LB address means a DNS change (`domains.md` holds which hostnames point where).
- **Stale ownerReferences.** A restored child whose owner's UID no longer matches is an orphan on the next garbage-collection sweep (`operators.md`). Restore owners before children, or let the controller recreate the children.
- **External state**: DNS records, cloud IAM bindings for workload identity, external secret-store entries, registry credentials. The cluster restores; the things it talks to do not.

## Volume Data

- CSI snapshots live in the same storage system as the volume by default. That is availability, not backup: the account, region, or storage system that fails takes both. A real backup is in a different failure domain and has a different credential.
- Application consistency needs quiescing: a pre-backup hook that flushes and freezes, a post-backup hook that resumes, or a logical dump instead. For databases, the operator's own backup path usually beats a generic volume snapshot (`stateful.md`).
- File-level backup (restic/kopia-class, copying from a mounted volume) works on storage with no snapshot support and is far slower on millions of small files. Snapshot when the driver supports it, file-level when it does not, and know which one your tool chose per volume.
- Restore into a **new** PVC and point a scratch pod at it before touching production. Restoring over a live volume is the operation people perform once.
- Retention with object-lock or immutability on the backup bucket is the only control that survives an attacker with cluster credentials — and the backup service account is a prime target precisely because it can read every Secret (`rbac.md`).

## etcd Snapshots (self-managed only)

- A snapshot is a single file taken from one member; restoring it creates a new cluster data directory that every member must be rebuilt from, with the API servers stopped throughout. It is a rebuild procedure, not a rollback button.
- It restores the world as of that instant: objects deleted after the snapshot come back, and objects created after it vanish. Controllers then reconcile toward whatever they find, which can mean deleting real workloads or recreating deleted ones.
- Encrypt it. An etcd snapshot contains every Secret in the cluster in whatever form etcd holds them — with no encryption-at-rest provider, that is plaintext (`config-and-secrets.md`).
- On managed control planes this section does not apply: the provider owns etcd, and your entire object-level plan is Git plus a backup operator.

## The Restore Rehearsal

The only test that counts, quarterly, into a scratch cluster or namespace:

1. Pick a real namespace with a PVC and at least one Secret.
2. Restore objects, then data, then check what did not come back — the list above is the checklist.
3. Time it end to end, including the part where someone finds the credentials for the backup store.
4. Bring up the workload and prove it serves, not that the pods are Running.
5. Record the measured RTO, and every gap found, in `deploys/<year>.md` under `## Restore Drills`. The RTO you may quote is the number from step 3, never the one in the plan.

A drill that finds nothing was too easy: restore into a cluster that does not already have the CRDs, or with the original namespace deleted, and it will find something.

## Designing For Recovery, Not For Backup

- RPO is decided by backup frequency, RTO by rehearsal. Both are business numbers before they are technical ones; write them down and size the schedule from them rather than accepting a tool's default.
- The fastest recovery is recreation: cluster from infrastructure-as-code, manifests from Git, data from backup. Every hour spent making the cluster reproducible removes an hour from every future restore.
- Keep the backup configuration itself in Git. A backup schedule that exists only inside the cluster it protects is not part of the plan.
- Test the restore path from a machine that is not the one that took the backup, using credentials that survive the incident. "The engineer with the credentials is on a plane" is a real RTO component.
- Deleting a CRD deletes every custom resource of its type cluster-wide, immediately (`operators.md`) — which is why CRD-owning operator upgrades belong in the same risk class as a restore, and get a backup taken first.

## Restore Gate

- Object backup and data backup both exist, and their schedules are known?
- Backup destination is in a different failure domain, with immutability or object-lock, and its own credential?
- Cluster-scoped objects (CRDs, StorageClasses, ClusterRoles, webhooks) included somewhere in the plan?
- Every Secret is either in a store outside the cluster or explicitly listed as needing manual recreation?
- Restore ordering documented: CRDs → namespaces → data → workloads → jobs?
- A restore was performed and timed this quarter, and its measured RTO is written in `deploys/<year>.md`?
- The gaps that drill found are either fixed or recorded in `## Known Gaps` with the date they were accepted?

Write the drill result — date, what was restored, measured RTO, what was missing — into `~/Clawic/data/k8s/deploys/<year>.md`, and set the next drill date in the `## Due` table of `memory.md`. An unrecorded drill is indistinguishable from no drill three months later, which is exactly when someone will ask for the RTO.
