const core = require('@actions/core');

function run(){
    try {
      const i_name = core.getInput('name');
      console.log(`Hello ${i_name}!`);
      core.setOutput("user_name", i_name);
    } catch (error) {
      core.setFailed(error.message);
    }
}

run();
