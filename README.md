# Second Mind Systems

AI can write and change software quickly. The difficult question is no longer only what an AI agent *can* do, but what it is *allowed* to change—and how a human can review what happened.

Second Mind Systems builds practical control and evidence tools for AI-assisted software work.

## Available now

### AI Protected Paths

AI Protected Paths adds an explicit local approval step before normal Git commits can modify files you designate as sensitive.

It is designed for solo builders and small teams working with AI coding agents around files such as authentication, billing, infrastructure, migrations, prompts, governance, and release configuration.

The current release provides:

- configurable protected-file boundaries;
- an explicit local approval-token workflow;
- blocking on the normal Git pre-commit path when approval is absent;
- local proof receipts for hook-governed commit decisions; and
- Windows and tested-host macOS validation, with native Linux validation still pending.

AI Protected Paths is available on Gumroad. The direct product link will be added here once its public URL is verified.

## Private pilot

We are also working directly with early users who want clearer control over AI-assisted changes without giving up the speed of coding agents.

A pilot may be a fit if your team is asking:

- Which files should an AI agent be allowed to change?
- When should a human approval be required?
- What evidence should remain after an AI-assisted change?
- How can we introduce useful friction without stopping development?

[Open a pilot inquiry](https://github.com/Secondmindsystems/second-mind-systems/issues/new) and describe your current workflow, the tools you use, and the change-control problem you are trying to solve.

## Evidence posture

We publish bounded claims and distinguish demonstrated product behavior from planned capabilities.

Current AI Protected Paths validation demonstrates that, in the tested local environments, normal commits to designated paths can be blocked without approval, allowed with explicit local approval, and recorded with a local receipt.

## Boundaries

AI Protected Paths is local Git governance friction. It is not:

- cryptographic or tamper-proof security;
- a replacement for code review, CI policy, access control, or branch protection;
- protection against `git commit --no-verify` or removal of the hook;
- guaranteed remote or organization-wide enforcement; or
- a claim that every supported operating system has completed native validation.

Second Mind Systems is early. We are publishing what exists, stating what it proves, and learning from real operator workflows.

## Rights

Copyright (c) 2026 Second Mind Systems. All rights reserved.

No license is granted to reproduce, adapt, distribute, or commercially use this material except with prior written permission. GitHub's applicable platform terms still govern use of the GitHub service.
