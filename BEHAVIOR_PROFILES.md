# Behavior Profiles

## The Meta Layer Behind AI Skills

### The Missing Behavioral Layer Between Capability and Governed Action

**Public Edition v0.2**

*By Second Mind Systems*

Copyright © 2026 Second Mind Systems. All rights reserved.

---

## From Models to Agents

For years, conversations about artificial intelligence centered on one question:

> **What can the model do?**

Can it write code?

Can it summarize documents?

Can it analyze contracts?

Can it build applications?

Can it reason?

That question made sense while AI systems primarily answered questions. But AI is changing.

Models are becoming agents.

They plan, edit, execute, call tools, modify repositories, and complete multi-step workflows. They increasingly participate in real work rather than isolated conversations.

That transition changes something fundamental.

Capability is no longer the only thing that matters.

Behavior becomes part of the system.

## AI Skills Changed What Agents Can Do

Skills have become an important building block of modern AI agents.

They provide reusable procedures for tasks such as:

- writing code;
- inspecting repositories;
- summarizing meetings;
- generating tests;
- deploying applications; and
- completing specialized workflows.

Skills dramatically expand what an AI agent can do.

But greater capability has also exposed a different engineering problem.

## A Different Kind of Failure Is Emerging

As agents become more capable, users continue encountering similar frustrations.

A one-file change becomes a repository-wide refactor.

An agent silently makes assumptions instead of asking a question.

It edits files that were never mentioned.

It performs cleanup nobody requested.

It presents speculation as established fact.

These failures do not necessarily occur because the agent lacks intelligence or technical capability.

They occur because the agent behaves poorly while using capabilities it already possesses.

> **Many modern AI failures are not capability failures. They are behavioral failures.**

Once capability is no longer the only bottleneck, conduct becomes an engineering problem of its own.

## Skills Are Not Behavior

Two agents with similar capabilities can produce very different working experiences.

One silently expands the task.

The other recognizes that adjacent improvements fall outside the requested boundary.

One finishes with a bare statement that the work is done.

The other makes its changes understandable and reviewable.

The technical capability may be the same.

The behavior is different.

And that difference changes the quality, risk, and review burden of the work.

Skills answer:

> **What should this agent know how to do?**

Behavior raises another question:

> **How should this agent conduct itself while doing the work?**

Skills expand capability.

Behavior Profiles govern conduct.

## Permissions Are Not Conduct

Capability, skills, permissions, behavior, and enforcement solve different problems.

**Capabilities** define what an agent is technically able to do.

**Skills** provide reusable procedures for performing work.

**Permissions** define which resources and operations the agent may access.

**Behavior Profiles** govern how the agent should conduct itself while using those capabilities, skills, and permissions.

**Enforcement** blocks, records, or escalates activity at declared boundaries.

These layers are related, but they are not interchangeable.

An agent may have permission to edit an entire repository while still being expected to modify only one file.

It may possess a deployment skill while still being expected to ask before initiating a release.

It may be capable of making a confident claim while still being expected to distinguish evidence from inference.

Permission establishes what is available.

Conduct governs how available power is used.

## The Missing Behavioral Layer

This suggests an architectural layer behind AI skills: a **Behavioral Layer**.

The Behavioral Layer does not give an agent another technical capability. It shapes how existing capabilities are used across different tasks.

It may govern dimensions such as:

- scope discipline;
- claim discipline;
- uncertainty;
- reviewability;
- escalation;
- evidence awareness;
- explicit handoffs; and
- preservation of human authority.

This layer surrounds skills rather than replacing them.

Capability determines what an agent can accomplish.

Behavior shapes how it approaches the work.

## Introducing Behavior Profiles

One expression of the Behavioral Layer is what Second Mind Systems calls a **Behavior Profile**.

A Behavior Profile is a durable behavioral specification that shapes how an agent conducts work across different tasks.

The task may change.

The expected conduct remains.

A coding skill might help an agent repair software. A research skill might help it investigate a question. A deployment skill might help it release an application.

A Behavior Profile addresses the conduct expected while any of those capabilities are being used.

Behavior Profiles therefore occupy a different layer from skills:

> Skills expand what an agent can do.
>
> Behavior Profiles govern how the agent conducts work.

## Why Prompt-Only Control Is Incomplete

Behavioral expectations are often scattered across task prompts, team conventions, memory, and human review.

That can work for simple interactions. It becomes less reliable as agents receive longer tasks, broader permissions, more tools, and greater autonomy.

Instructions may be interpreted inconsistently. Expectations may disappear between tasks. Human reviewers may discover boundary violations only after changes have already been made.

Behavior Profiles frame conduct as a persistent design concern rather than an incidental sentence inside a prompt.

This does not mean a profile automatically enforces its own expectations.

Behavioral specification and deterministic enforcement remain different layers.

## Scope Control as a Conceptual Example

Consider a request to fix a typo in one documentation file.

A capable agent may also notice adjacent formatting issues, outdated examples, or opportunities to reorganize nearby content.

Those improvements may be reasonable. They were not necessarily authorized.

A Scope Control profile asks an agent to distinguish the authorized task from adjacent improvements it merely notices.

The goal is not to prevent useful initiative. It is to ensure that expanding scope becomes an explicit decision rather than a silent assumption.

The resulting edit may look nearly identical.

The difference is accountability.

## Reviewability Changes the Trust Equation

Behavior alone is difficult to trust when it remains invisible.

Trust becomes easier when work is inspectable.

A human reviewer benefits from knowing:

- what changed;
- why it changed;
- what remains uncertain; and
- whether important boundaries were encountered.

Reviewability does not guarantee correctness.

It makes correctness, error, and overreach easier to evaluate.

That distinction matters because trustworthy AI-assisted work may depend less on pretending every output is perfect and more on making consequential work legible to the people responsible for it.

## Behavior → Reviewability → Enforcement

As agentic systems mature, a natural progression emerges:

> **Behavior → Reviewability → Enforcement**

First, expected conduct is defined.

Then, conduct and outcomes become inspectable.

Finally, important boundaries receive explicit controls that block, record, or escalate activity.

Behavior establishes expectations.

Reviewability makes conduct visible.

Enforcement protects declared boundaries.

None of these layers replaces the others.

A behavioral expectation without reviewability can be difficult to trust. Reviewability without enforcement may reveal a violation only after it occurs. Enforcement without a clear behavioral model may block actions without explaining the larger operating intent.

Together, they form a more complete approach to governed AI-assisted work.

## Protected Paths as a Bounded Enforcement Primitive

AI Protected Paths is one practical Second Mind Systems engineering artifact positioned further along this progression. Its public evidence package is currently being reconciled against the independently tested v1.0.1 release boundary.

It governs designated files at the normal local Git commit boundary.

In tested environments, normal commits touching designated paths can be blocked when explicit local approval is absent, allowed when that approval is present, and accompanied by a local proof receipt.

Its scope is intentionally bounded.

AI Protected Paths is not cryptographic security, tamper-proof enforcement, branch protection, or guaranteed remote or organization-wide control. It does not prevent bypass through `git commit --no-verify` or removal of the hook.

It is a practical local enforcement primitive: explicit friction around declared files during the normal commit workflow.

Behavior Profiles describe expected conduct.

Protected Paths demonstrates one bounded way that a declared boundary can receive deterministic local enforcement.

## What Second Mind Systems Has Demonstrated

Second Mind Systems has publicly released AI Protected Paths and validated its core local commit-boundary behavior in the stated tested environments.

Second Mind Systems has also developed the Behavior Profiles category thesis and private behavioral-governance artifacts.

This public paper establishes the conceptual category and its relationship to governed AI-assisted work.

It does not demonstrate or claim:

- a universally validated behavioral standard;
- a public profile compiler;
- a public composition or selection system;
- a general-purpose orchestration runtime;
- universal behavioral compliance;
- complete enforcement across tools or environments; or
- customer or product-market validation for the broader category.

Those distinctions are intentional.

A positioning paper establishes an argument.

A product demonstrates bounded behavior.

Broader claims require broader evidence.

## Proprietary Implementation Boundary

This paper explains what the Behavioral Layer is and why it matters.

It does not disclose the proprietary machinery used to construct, persist, compose, select, evaluate, orchestrate, or enforce Behavior Profiles.

Complete profiles, installation methods, operating procedures, evaluation systems, enforcement architecture, and runtime mechanisms remain private to Second Mind Systems unless explicitly released under separate terms.

The public category thesis should be understandable.

The implementation does not need to be reconstructable.

## A Different Way to Evaluate AI

For years, AI systems have largely been evaluated by what they can do.

That remains important.

As those systems participate more deeply in real work, another question becomes equally important:

> **How does your AI behave while doing it?**

That question points toward a missing layer between capability and governed action.

One that sits behind skills.

One that shapes conduct.

One that makes work more reviewable.

One that can connect behavioral intent to meaningful boundaries.

The first generation of AI largely competed on intelligence and capability.

The next generation may increasingly compete on conduct, reviewability, and trust.

Behavior Profiles are Second Mind Systems' name for that emerging layer.
