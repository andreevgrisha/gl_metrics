GL testlab.

Collect metrics python script.
Run with parameter to specify wich metrics gathering:

>python3 metrics.py ARG

Dockerfile for package and execute script in container:

>docker build -t metrics .

Please run container with --pid=host namespace setting:

>docker run --rm --pid=host metrics ARG 

ARG will be "cpu" or "mem".
