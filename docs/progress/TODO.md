# Paksa Financial System - Delivery Backlog

This backlog tracks execution tasks. Canonical status lives in `docs/progress/MASTER_STATUS.md`.

## I. Governance & Reliability (Priority 1)
- [ ] Align legacy status documents with `MASTER_STATUS.md`
- [x] Add release-governance checklist to deployment process
- [x] Add migration smoke test in CI/CD
- [x] Add tenant-isolation regression checks
- [ ] Add backup/restore smoke test to release gate

## II. Core Financial Completion (Priority 1)
- [ ] General Ledger: reporting + period close completion
- [ ] Budget Management: advanced controls + approval workflow completion
- [ ] Validate AP/AR/Cash Management end-to-end workflows with integration tests

## III. Cross-Cutting Controls (Priority 2)
- [ ] Define and track production SLOs (availability, p95 latency, error budget)
- [ ] Complete compliance hardening and audit logging verification
- [ ] Create incident response runbook and escalation matrix

## IV. Product & Analytics (Priority 3)
- [ ] AI/BI dashboards fully backed by real datasets
- [ ] Advanced financial reporting & consolidation
- [ ] User training guides for newly completed modules
