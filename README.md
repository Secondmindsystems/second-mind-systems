# Second Mind Systems

## Governed Repo — One Change. Two Gates. One Receipt.

**Working code is not always acceptable work.**

Code review asks whether a change works. Governed Repo also checks whether it was authorized, stayed in bounds, and made only claims the evidence supports.

An AI can produce a technically valid repository change that still exceeds its assignment, touches the wrong files, or makes claims its evidence does not support.

**Governed Repo checks those conditions before the change is trusted.**

**[Run the five-minute demo](https://github.com/Secondmindsystems/governed-change-demo)** · **[Inspect the evidence portfolio](https://github.com/Secondmindsystems/governed-ai-systems-portfolio)**

> The public demonstration proves deterministic evaluation of declared change snapshots and hash-linked receipt generation under fixed inputs and policies. It does not establish security, production readiness, live repository enforcement, customer validation, or execution authority.

## What changes operationally

Without an explicit control boundary, a change can pass technical tests while its real failures remain buried in the diff, prompt history, repository settings, evidence, or reviewer judgment.

Governed Repo makes those failures produce a visible result:

```text
technically valid + outside authority
→ BLOCK

technically valid + wrong repository path
→ BLOCK

technically valid + claims the evidence does not support
→ BLOCK

repaired + completely rechecked + aligned
→ PASS
```

A blocked change is not overwritten or quietly approved later.

The repair becomes a new revision, re-enters through the authority and context check, reruns both gates, and preserves the earlier `BLOCK` in a linked receipt.

The change does not count merely because the code works. The declared authority, repository boundaries, claims, evidence, and policies must align.

## The executable episode

A **declared snapshot** is a frozen, complete description of a proposed repository change.

The public demonstration evaluates one such snapshot.

Its central fixture begins with an AI-assisted change that creates two independent failures:

1. It proposes writing to `config/production-mode.json`, outside the declared path authority.
2. It claims, “This repository change is production-ready and secure for customer deployment,” even though the declared evidence does not support that claim or include its required limitations.

This is not an illustrative scenario. It is the public demo’s actual blocked fixture.

The code itself may be technically plausible. The proposed change still returns:

```text
CAP — authority and context precheck:  PASS
Path Gate — where it writes:           BLOCK
Claims Gate — what it asserts:         BLOCK
Combined result:                       BLOCK
```

The repair:

* removes the unauthorized configuration operation;
* moves the permitted edit to `docs/public/governed-change-result.md`;
* narrows the production and security claim to a bounded process description that the evidence supports;
* increments the revision;
* reruns the authority and context check;
* reruns both domain gates.

The repaired revision returns:

```text
CAP — authority and context precheck:  PASS
Path Gate — where it writes:           PASS
Claims Gate — what it asserts:         PASS
Combined result:                       PASS
```

The `PASS` receipt links to the earlier `BLOCK` receipt by both receipt ID and full SHA-256 hash.

The accepted result therefore preserves not only what passed, but what originally failed and why.

Clone the repository, run the demonstration, and reproduce the same `BLOCK`, bounded repair, complete re-evaluation, and linked `PASS` receipt on your machine.

**[Run it now](https://github.com/Secondmindsystems/governed-change-demo)**

## Why this matters

Most AI-assisted repository changes are ordinary.

The risk lies in the smaller set that looks technically plausible while crossing a boundary that was never made explicit—or asserting more than the evidence can support.

Examples include:

* a workflow file that broadens deployment permissions;
* a release note claiming tests passed when no closed test evidence exists;
* an AI change touching authentication, billing, infrastructure, or migration files outside its assignment;
* generated documentation claiming security or production readiness without supporting evidence;
* a governance or approval file that weakens the checks governing the change.

Governed Repo makes those boundaries and evidence gaps visible before the change is accepted.

It checks:

* whether the proposed work is authorized;
* whether it writes only where it is allowed;
* whether its claims are supported by the declared evidence;
* whether required limitations are present;
* whether every required check actually ran;
* and what record should remain after the decision.

The current public demo evaluates declared snapshots representing these situations. It does not inspect, enforce, or modify a live worktree.

## What Governed Repo makes reviewable

Governed Repo brings the information needed to judge one proposed change into a single reviewable process.

It makes visible:

* **Authority** — who is permitted to propose the work and what they were permitted to do.
* **Scope** — which repository locations and operations the change is allowed to affect.
* **Claims** — what the changed material says and whether the declared evidence supports it.
* **Readiness** — whether the required context, policies, evidence, and checks are present and current.
* **Decision completeness** — whether every required condition was evaluated before the result became `BLOCK`, `HOLD`, or `PASS`.
* **Repair history** — what originally failed, what changed in the repair, and whether the full evaluation ran again.
* **Decision evidence** — what was examined, which boundaries applied, what the outcome was, and why it counted.

The result is not merely another review report.

It is a visible acceptance boundary: the change does not count simply because the code works.

```text
proposed change
→ authority, scope, and evidence checked
→ BLOCK, HOLD, or PASS
→ repair fully rechecked
→ decision history preserved
```

Governed Repo does not execute the change or grant permission to execute it.

## Why this is technically non-trivial

* Permission, repository policy, and supporting evidence are different questions.
* Path and claim evaluation require materially different policy logic.
* A skipped, unavailable, malformed, or stale check cannot silently become `PASS`.
* Claims must be evaluated against declared evidence rather than accepted because they sound plausible.
* A repaired revision must re-enter through the authority and context precheck rather than resume after the failed gate.
* A later `PASS` must preserve the earlier `BLOCK` rather than overwrite it.
* Fixed inputs, evaluator versions, policies, evidence, and evaluation time must reproduce the same decision and canonical receipt.
* Public claims about the demonstration are bound to machine-readable evidence and checked in CI rather than maintained only as prose.

This is not one scanner with several labels.

It is a staged acceptance process in which distinct checks retain their own evidence while contributing to one reviewable disposition.

## What you can verify now

The standalone [Governed Change Demo](https://github.com/Secondmindsystems/governed-change-demo) uses only Python’s standard library and includes:

* six strict JSON contracts;
* a Context and Authority Precheck;
* two independent policy gates;
* deterministic `BLOCK → repair → PASS`;
* fail-closed `BLOCK` and `HOLD` cases;
* evidence-aware claims evaluation;
* hash-linked governed receipts;
* 76 automated tests;
* a machine-readable public claims manifest;
* a claims-manifest verifier;
* and a GitHub Actions validation workflow.

The published instructions have been reproduced from a clean network clone with 76 of 76 tests passing.

Expected replay identity:

```text
sha256:10a2135e3e8127ab8ed9d17759d8507e424d0aba2ad73afaa183bf9cf00778f4
```

Independent third-party reproduction on separate hardware remains pending.

**[Run the demo and return PASS, FAIL, or CONFUSED](https://github.com/Secondmindsystems/governed-change-demo/issues/1)**

The [Governed AI Systems Portfolio](https://github.com/Secondmindsystems/governed-ai-systems-portfolio) provides the broader architecture, sanitized receipts, bounded public claims, verification record, and limitations.

## What has been demonstrated

* Deterministic evaluation for fixed fixtures, policies, evaluator versions, evidence, and evaluation time.
* Two materially different gates operating on one shared description of the proposed change.
* Fail-closed authority, context, path, claim, evidence, and malformed-input outcomes.
* A visible blocked revision followed by a bounded repaired revision.
* Complete authority, context, and gate re-evaluation after repair.
* Claims narrowed to what the declared evidence supports.
* Receipt linkage preserving the earlier decision.
* Byte-identical replay.
* Clean-clone execution of the published commands.
* Machine-verifiable binding between public claims and demonstration evidence.
* Public evidence-packet integrity checking for the portfolio.
* Local AI Protected Paths behavior in its stated tested environments.

## What has not been demonstrated

* Production or deployment readiness.
* Security, tamper resistance, branch protection, certification, or regulatory compliance.
* Live worktree enforcement or automatic repository mutation by the public demo.
* Multi-agent, concurrent, high-scale, or production adversarial robustness.
* Production performance, capacity, availability, or latency.
* Customer adoption, market demand, or independent third-party validation.
* General authorization to execute repository changes.
* That a receipt automatically makes a claim true, grants authority, or creates trust.

## Related engineering systems and controls

### Governed Repo

Governed Repo makes the authority, repository boundaries, claims, evidence, decision, and repair history of an AI-assisted change reviewable before the change is trusted.

The public demonstration evaluates declared change snapshots. The broader private MVP extends the same control pattern to a read-only view of live repository state.

### AI Protected Paths

AI Protected Paths adds an explicit local approval step before normal Git commits can modify files designated as sensitive.

It creates commit-time friction around configured paths such as authentication, billing, infrastructure, migrations, prompts, governance, and release configuration.

It provides:

* configurable protected-file boundaries;
* an explicit local approval-token workflow;
* blocking on the normal Git pre-commit path when approval is absent;
* and local proof receipts for hook-governed commit decisions.

Protected Paths is a prior engineering artifact. Its public evidence package
is being reconciled against the independently tested v1.0.1 release boundary;
no commercial download link is currently offered here.

AI Protected Paths is not cryptographic security, remote organization-wide enforcement, branch protection, or protection against `git commit --no-verify` or hook removal.

### Behavior Profiles

**Skills describe what an agent knows how to do.**

Behavior Profiles describe how the agent is expected to conduct itself while using those skills—including how it handles scope, uncertainty, authority, evidence, escalation, and stopping conditions.

A coding skill may know how to modify a repository. A Behavior Profile can require the agent to remain within the assignment, surface uncertainty, preserve evidence, and stop before crossing an authority boundary.

Read: [Behavior Profiles — The Meta Layer Behind AI Skills](BEHAVIOR_PROFILES.md).

This paper presents a category argument. It does not claim a validated universal behavioral standard or complete general-purpose enforcement runtime.

### Surface

Surface is an advisory product-intelligence instrument used to pressure-test positioning, documentation, claims, packaging, and readiness.

Surface is currently used inside our own product reviews.

**A public version is coming soon.**

It is not part of Governed Repo’s deterministic repository-policy path.

## The broader direction

As AI agents become capable of making larger and faster changes, technical capability alone is not enough.

Organizations also need infrastructure that makes authority, scope, policy, evidence, agent conduct, and decision history visible before automated work is accepted.

The products above approach that problem from different operating points:

* Behavior Profiles shape how agents are expected to use their skills.
* Surface exposes problems in understanding, claims, packaging, and readiness.
* Governed Repo evaluates whether proposed work should be accepted.
* AI Protected Paths creates an explicit local checkpoint before sensitive changes are committed.

Together, they point toward a broader control layer for keeping increasingly capable AI work bounded, reviewable, attributable, and evidence-backed.

The public artifacts demonstrate bounded parts of that direction. They do not establish enterprise readiness, production enforcement, organization-wide deployment, or regulatory compliance.

## Work with us

We are interested in working with teams that are beginning to ask:

* Which actions should an AI agent be allowed to take?
* How should agents conduct themselves while using increasingly powerful skills?
* Which repository changes require an explicit human checkpoint?
* How should authority, scope, evidence, and limitations be declared before automated work is accepted?
* What decision record should remain after work is blocked, repaired, or approved?

Relevant engagements may include:

* a private Governed Repo pilot around a real repository workflow;
* evaluation of an existing AI-assisted change process;
* collaboration on governed-agent infrastructure;
* technical or product-design partnerships;
* strategic conversations with organizations or investors aligned with verifiable AI control systems.

The public demo is a bounded proof of the control pattern.

Private work can explore how those controls apply to a specific team, repository, or agent workflow.

**[Open a private pilot or collaboration inquiry](https://github.com/Secondmindsystems/second-mind-systems/issues/new)** and describe the workflow, tools, and control problem involved.

## Closing

Most AI-assisted repository changes are ordinary and can move through normal review.

The problem is the smaller set that looks fine while crossing a line no one drew—or claiming more than the evidence can carry.

Governed Repo makes that set visible, evaluates it, and preserves why the result counted.

**[Run the five-minute demo](https://github.com/Secondmindsystems/governed-change-demo)** · **[Inspect the evidence](https://github.com/Secondmindsystems/governed-ai-systems-portfolio)** · **[Report PASS, FAIL, or CONFUSED](https://github.com/Secondmindsystems/governed-change-demo/issues/1)**

## Authorship and AI collaboration

I defined the objectives, system architecture, authority model, constraints, acceptance gates, evidence requirements, claim limits, and integration decisions.

AI agents performed bounded implementation, analysis, drafting, testing, and review work under those controls.

Receipts preserve inspectable evidence.

## Rights

Copyright © 2026 Second Mind Systems. All rights reserved.

No license is granted to reproduce, adapt, distribute, or commercially use this repository’s proprietary written material except with prior written permission.

Separate repositories and products may carry their own licenses and terms.
