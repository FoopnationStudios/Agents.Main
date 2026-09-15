# Specialist Software Agent Standard

This policy applies only when `.ai/PROJECT.md` declares:

`Project-Type: SPECIALIST_AGENT`

A **specialist software agent** is a dedicated software product built to perform one bounded job or workflow with high repeatability. It is not merely a prompt, chat, dashboard, or general-purpose AI assistant.

## Core doctrine

> **AI FOR JUDGMENT. CODE FOR ENFORCEMENT. AUTHORITATIVE DATA FOR FACTS. QA FOR PROOF.**

The objective is not to claim zero error. The objective is to reduce discretionary solution space, make important rules explicit and enforceable, make outputs testable, and keep failure modes visible.

## Agent Contract

Before substantive implementation, define or reconcile the project's Agent Contract in `.ai/PROJECT.md` or another explicitly referenced canonical project file.

The contract must identify:

- **Job:** the single primary job the agent performs;
- **Inputs:** the information, files, events, or requests it may accept;
- **Outputs:** the artifacts, decisions, actions, or state changes it may produce;
- **Authority:** what it may do autonomously;
- **Human gates:** what requires operator approval;
- **Non-goals:** what is explicitly outside scope;
- **Sources of truth:** which files, APIs, databases, rules, templates, or external systems are authoritative;
- **Failure behavior:** what happens when information is missing, contradictory, stale, invalid, or outside scope;
- **Success standard:** how correctness and usefulness will be measured.

If the job cannot be bounded well enough to define this contract, do not silently broaden the system. Clarify the scope before treating it as a specialist agent.

## Mandatory architecture separation

For every significant responsibility, explicitly decide which layer owns it.

### 1. AI judgment

Use the model where interpretation, synthesis, classification, extraction, prioritization, drafting, or other non-deterministic reasoning is genuinely useful.

The model must not invent missing operational facts. When evidence is insufficient, preserve uncertainty or escalate according to the Agent Contract.

### 2. Deterministic enforcement

If a requirement should always behave the same way, encode it in software, configuration, schema, or validation whenever practical.

Typical examples include:

- required fields;
- formatting;
- calculations;
- date/time transformations;
- file naming;
- schema enforcement;
- duplicate detection;
- ordering;
- thresholds;
- permissions;
- allowed workflow transitions;
- API argument validation;
- fixed output structure.

Do not rely on prompt memory for deterministic requirements that software can enforce.

### 3. Authoritative data and tools

Material facts should come from approved authoritative sources when one exists. Examples include APIs, databases, confirmations, account state, published platform data, market data, mapping data, or other canonical records.

The agent must distinguish retrieved facts from inference.

### 4. Persistent state

Information that must survive beyond one model call or chat session belongs in durable state rather than conversational memory alone.

Examples include project state, prior outputs, approvals, audit logs, settings, performance history, workflow status, and business records.

### 5. Validation and QA

Important outputs must be validated before acceptance. Validation may include schema checks, deterministic rule checks, completeness checks, cross-source reconciliation, regression tests, golden-output comparison, adversarial cases, model evaluations, or human review where judgment remains consequential.

### 6. Interface

The dashboard or UI is the operator's interface to the agent, not the source of its intelligence. The normal workflow should expose inputs, current state, exceptions, review points, and outputs without requiring the operator to understand repository internals.

Prefer the simplest interface that makes the bounded workflow obvious.

## Anti-drift rule

For every important requirement ask:

> **Does the AI need discretion here?**

- **NO:** move the requirement into code, configuration, schema, validation, or another deterministic mechanism whenever practical.
- **YES:** document the reasoning doctrine, provide the required evidence and tools, constrain the available actions, make the decision auditable, and test representative cases.

Project conversations may evolve without silently changing production behavior. Approved behavior changes must be reflected in canonical repository artifacts and, where practical, tests.

## Build sequence

Unless a documented project constraint requires otherwise, use this sequence:

1. **Inspect** — read the existing repository and preserve useful work. Do not restart solely because this policy was introduced later.
2. **Contract** — define or reconcile the Agent Contract.
3. **Decompose** — classify responsibilities into AI judgment, deterministic code, authoritative data/tools, persistent state, QA, and interface.
4. **Harden the SSOT** — move durable approved rules and state into canonical repository artifacts rather than leaving critical requirements only in chat history.
5. **Build the smallest end-to-end workflow** — implement the narrowest realistic path from input to output before broad feature expansion.
6. **Build validation** — create validators and tests for the requirements that matter most.
7. **Test realistic cases** — include at least a normal case, incomplete input, contradictory input, malformed input, an edge case, and a known prior failure when available.
8. **Measure** — define domain-appropriate success metrics such as accuracy, format compliance, reconciliation accuracy, task completion rate, manual corrections, latency, cost, or business outcomes.
9. **Pilot** — run realistic workflows with human review and record failures.
10. **Iterate by failure mode** — fix the correct layer rather than repeatedly adding prompt text.

## Failure classification

When the agent fails, classify the failure before changing the architecture:

- reasoning failure;
- missing or incorrect source data;
- deterministic-rule gap;
- validator gap;
- state/memory failure;
- UX/operator error;
- integration failure;
- scope/design failure.

A prompt change is not the default fix for every failure.

## Scope expansion

A successful specialist agent may grow, but adjacent functionality is not automatically in scope.

Before expanding, determine whether the new job substantially shares the same inputs, doctrine, state, permissions, and output workflow. If not, prefer a separate specialist agent or service and integrate them intentionally if needed.

Avoid gradually turning a bounded agent into a generalized "do everything" system.

## Required project artifacts

Adapt exact filenames to the project, but a mature specialist agent should establish equivalents of:

- the root `AGENTS.md` and standard `.ai/` governance control plane;
- an explicit Agent Contract;
- project-specific architecture showing the six-layer separation above;
- domain doctrine for expert judgment;
- machine-readable configuration where stable rules benefit from it;
- schemas for important inputs and outputs;
- deterministic validators;
- automated tests;
- representative fixtures or golden examples;
- defined failure and exception behavior;
- durable state where the workflow requires it.

Do not create artifacts merely to satisfy a checklist. Each must serve the project.

## Controller adoption behavior

When a controller inherits an existing specialist-agent project, it must:

1. follow the normal `AGENTS.md` boot sequence;
2. read this file because `Project-Type` is `SPECIALIST_AGENT`;
3. inspect the actual project state and any R&D/product handoff;
4. preserve useful existing work;
5. define or reconcile the Agent Contract from the available project context;
6. map current behavior into the six architecture layers;
7. identify where LLM interpretation is being used for rules that should be deterministic;
8. identify missing authoritative data sources and validation;
9. implement the minimum coherent architecture changes required;
10. continue from current state rather than rebuilding unnecessarily.

The owner should not need to issue a special bootstrap prompt beyond the normal instruction to adopt the project, read the handoff, and read the repository.

## Acceptance standard

A project is not a mature specialist agent merely because it contains an LLM and a dashboard.

A mature specialist agent should demonstrate that:

- its primary job is bounded and explicit;
- its allowed inputs and outputs are understood;
- its doctrine and durable rules are canonical and versioned;
- deterministic rules are mechanically enforced where practical;
- material facts come from appropriate sources;
- important state persists outside transient conversation context;
- important outputs are validated;
- representative tests exist;
- failure behavior is defined;
- its operator can understand and control the workflow through a fit-for-purpose interface;
- changes remain governed through the project repository;
- the system materially reduces manual effort, increases reliability, or both for its intended job.
