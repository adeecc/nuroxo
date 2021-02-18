import aiml
import os

class NuroxoChatBotBase:
    def __init__(self, session_id, **kwargs) -> None:
        # Set Current Session ID
        self.session_id = session_id

        # Create new Kernel
        self.kernel = aiml.Kernel()

        # Set file path for brain file. This will be loaded if it exists or created.
        file_path = os.path.join("static/brains/", f"bot_{self.session_id}.brn")

        # If brainfile exists, load. Else Create new
        if os.path.isfile(file_path):
            self.kernel.bootstrap(brainFile=file_path)

        else:
            self.kernel.bootstrap(learnFiles=os.path.join("static", "std-startup.xml"), commands="load aiml b")

        # Update the brain file with more preicates
        if kwargs:
            self.set_predicates(**kwargs)

        # Save the brain file after adding new predicates
        self.kernel.saveBrain(file_path)
        

    def set_predicates(self, **kwargs):
        for key in kwargs:
            self.kernel.setPredicate(key, kwargs.get(key), self.session_id)
    

    def reply(self, msg: str):
        return self.kernel.respond(msg, self.session_id)


