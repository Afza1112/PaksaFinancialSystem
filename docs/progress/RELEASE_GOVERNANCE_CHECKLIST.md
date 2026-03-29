# Release Governance Checklist

Use this checklist before every production release.

## 1) Status and Scope
- [ ] Release scope documented and approved.
- [ ] Status reflects `docs/progress/MASTER_STATUS.md`.
- [ ] Change log and rollback owner assigned.

## 2) CI Evidence Gates
- [ ] Linting passes.
- [ ] Security checks pass.
- [ ] Unit/integration/security tests pass.
- [ ] Coverage threshold is met.
- [ ] Migration smoke test passes.
- [ ] Tenant-isolation regression test passes.

## 3) Database and Data Safety
- [ ] Backup created before deployment.
- [ ] Restore smoke test executed in non-production environment.
- [ ] Migration plan validated for forward-only deployment.

## 4) Runtime Readiness
- [ ] Health checks are green.
- [ ] Alerting channels verified.
- [ ] SLO watch window defined for post-release monitoring.

## 5) Sign-off
- [ ] Engineering lead sign-off
- [ ] DevOps lead sign-off
- [ ] Product/Operations sign-off
