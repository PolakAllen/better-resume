better-resume
=============

There's no escaping a need for resumes in today's age, but usually they're very
inefficent.

Very few will actually *read* a resume, and very often its just a gatekeeper,
with rejections based off of first-and-only impressions

In technical areas however, there's a real need to understand someone's level of
experience with a particular skillset or technology. 

Most resumes simply blindly list which skillsets they have; some even go so far
to list some measure of experience. However, none of them are very good
indicators, without painstainking descriptions of what you actually did.

Attempting to list all of our experience would generate far too much content for
a resume.

Ideally we could tailor our experiences an employer's desired skillset. But
doing so is extremely difficult.

*Until now*

Better resume is still a work in progress, but the key idea is being able to
list and aggregate all of your personal experience, and provide multiple outputs
for doing so.

To use:

    unzip and start writing your experience
      src/data/raw.yaml
        cv:
          intro:
            title:
            content:
          personal: {name,address,phone,email,website}
          jobs: 
            -
              employer:
              location:
              positions: [{time,title,projects,tasks}]
          education: [{name,location,time,degree,gpa}]
          extra: [projects,activities,organizations,research]

    customize just about everything
    python src/main.py
