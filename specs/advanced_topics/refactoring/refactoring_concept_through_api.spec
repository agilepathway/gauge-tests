Refactoring Concept through API
===============================

tags: refactoring, api, java, csharp, ruby, python, js

* Initialize a project named "refactor_concept_thru_api" without example spec
* Create concept "concept with <param0> and <param1>" with following steps 

   |concept steps                            |
   |-----------------------------------------|
   |nested concept with <param0> and <param1>|
   |simple step with "static"                |

* Create concept "concept" with following steps 

   |concept steps            |
   |-------------------------|
   |simple step with "static"|

* Start Gauge daemon

Rename concept
--------------

* Refactor step "concept" to "refactored concept" via api
* The step "refactored concept" should be used in project
* The step "concept" should no longer be used

Rephrase concept with removal of params
---------------------------------------

* Refactor step "concept with <param0> and <param1>" to "concept with <param0>" via api
* The step "concept with <param0>" should be used in project
* The step "concept with <param0> and <param1>" should no longer be used

Rephrase concept with addition of params
----------------------------------------

* Refactor step "concept with <param0> and <param1>" to "concept with <param0> and <param1> and <param2>" via api
* The step "concept with <param0> and <param1> and <param2>" should be used in project
* The step "concept with <param0> and <param1>" should no longer be used

Rephrase concept
----------------

* Refactor step "concept with <param0> and <param1>" to "concept with <param0> and <param2>" via api
* The step "concept with <param0> and <param2>" should be used in project
* The step "concept with <param0> and <param1>" should no longer be used

____________
* Stop Gauge daemon