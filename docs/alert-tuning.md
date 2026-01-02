## Alert Tuning Overview

Initial alert rules may generate false positives.
Alert tuning is the process of refining detection logic
to improve accuracy while maintaining visibility.

## False Positive Analysis

The brute-force alert may trigger when:
- A legitimate user mistypes their password multiple times
- Network latency causes retry behavior

These scenarios are not malicious but generate alerts.

## Rule Improvement

To reduce false positives:
- Increase failed login threshold
- Require repeated behavior across sessions
- Combine with additional indicators such as IP reputation

## Severity Tuning

Initial alerts are classified as Medium severity.
After tuning, alerts should be escalated only
if additional suspicious behavior is observed.
