Custom Screenshot
=================

tags: java, csharp, ruby, python, js

Screenshot using custom logic
-----------------------------

* Initialize a project named "custom_screenshot" without example spec

* Configure project to take custom screenshot and return "some screenshot" as byte array

* Create a specification "custom_screenshot" with the following contexts 

   |step text |implementation     |
   |----------|-------------------|
   |hello step|"inside hello step"|

* Create a scenario "generate custom screenshot" in specification "custom_screenshot" with the following steps with implementation 

   |step text  |implementation |
   |-----------|---------------|
   |Second step|throw exception|

* Execute the current project and ensure failure

* Generated html report should have "some screenshot" in spec "custom_screenshot" for

   |step text  |
   |-----------|
   |Second step|

