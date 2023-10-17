FROM ubuntu:latest
COPY github_env.bash /github_env.bash
RUN chmod +x ./github_env.bash
ENTRYPOINT ["/github_env.bash"]
