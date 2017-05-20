# Configure vscode Test task with pytest

This repository gives a simple example how
to configure the problem matcher for a `Test Task` of
`vscode` in order to get the test failures and other
issues into the `problems view` and highlighted in the `code view`.

See [.vscode/tasks.json](./.vscode/tasks.json) file to see how
`pytest` and problem matchers are configured.

### At project start

![](./.imgs/vscode_test_not_run_yet.png)

### Run Configured Test Task

![](./.imgs/vscode_select_run_test_task.png)

### See errors in the problem view and code
![](./.imgs/vscode_test_ran_problems_view.png)

### Text from the Output view is parsed
![](./.imgs/vscode_test_ran_output_view.png)

### Outstanding issues
> NOTE: file names are not clickable in the Output view.
There's an outstanding issue on https://github.com/Microsoft/vscode/issues/586
"Link to a file position in Output Channel".
It is note immediately obvious that it is the related issue,
but another issue https://github.com/Microsoft/vscode/issues/5583
"Make the error message in the output window clickable to navigate to the error position. " was consolidated into this.

> NOTE: the multi-line problem matcher does not let to capture
a message spread across multiple lines. There's an outstanding issue for this. https://github.com/Microsoft/vscode/issues/9635
"Problem matchers for error messages that span multiple lines #9635"

