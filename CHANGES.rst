Changelog
=========

0.7.0 (unreleased)
------------------

* Portlets can work on Plone4 and on Plone5
* URL preview test do not fetch remote resources to avoid timeout
  [ale-rt]

* merge "Conversation" sprint reply-to-statusupdate

* "Berlin" sprint frontend rewrite based on patternslib


0.5.4 (unreleased)
------------------

* use UID from brain Don't do getobject
  [maartenkling]

* add url preview tool that adapts StatusUpdate and returns list of image links
  [amleczko]

0.5.3 (2014-03-11)
------------------

* Package distribution was fixed by adding classifiers, dependencies and
  fixing license version number as GPLv2; a MANIFEST.in file was also added.
  [hvelarde]

* Brazilian Portuguese translation was added.
  [hvelarde]

0.5.2 (2013-07-31)
------------------

* bump version after having pypi release confusion [gyst]
* use backwardly compatible accessor [gyst]
* trust context=None defaults [gyst]
* French translation [tdesvenain]
* Few fixes on microblog context when we are in subfolders of context [tdesvenain]

0.5.0rc1 (2013-07-04)
---------------------

* update docs [gyst]
* finish IMicroblogContext implementation [gyst]
* provide upgrade step to add uuid mapping on older installed microblog tool [gyst]
* implement IMicroblogContext acquisition and storage for StatusUpdate [gyst, tdesvenain]
* Simplify API to filter on either user or context, but not on both. Cleanup and restructure implementation [gyst]
* fix testing thread cleanup [gyst]
* reword IMicroblogContext behavior [gyst]
* add a behaviour for IMicroblogContext local microblog support interface [tdesvenain]
* define IMicroblogContext interface as integration hook for local workspaces [gyst]
* fix flake8 errors [gyst]
* implement and integrate context permission checks for local microblog spaces [gyst]
* context filtering by uuid [gyst]
* integration test with actual plone.app.uuid resolving [gyst]
* refactor to (mocked) plone.app.uuid integration [gyst]
* base implementation for context-aware statuscontainer [gyst]


0.4.2 (2013-04-29)
------------------

* Plone 4.3 compatiblity [tdesvenain]

0.4.1 (2012-11-26)
------------------

* update changelog, release [gyst]
* update travis config to new buildout [gyst]
* provide a virtualenv-enabled Travis buildout that can be debugged on a dev box [gyst]
* Added l10n for English and Dutch for plone domain [macagua]
* Updated Spanish l10n [macagua]
* Updated sync i18n script with plone domain, added i18n for portlets, Generic Setup register Profile [macagua]
* Updated changelog contributors files and sync i18n script with plone domain, added i18n for portlets, Generic Setup register Profile [macagua]
* Makefile changes [avelino]
* pep8 and cleanups [avelino]
* pep8/pyflakes [gyst]
* update Travis CI configuration to include pep8/pyflakes testing [hvelarde]
* update location of extended configuration as the plonetest repo was moved to GitHub [hvelarde]
* update list of ignored objects [hvelarde]
* update doc, bump version [gyst]
* cleanup buildout [gyst]
* add Travis CI configuration [hvelarde]


0.4 (2012-10-09)
----------------

* .gitignores [gyst]
* update docs [gyst]
* fix dependency [gyst]
* reindent for better pep8 [gyst]
* s/_flush_queue/flush_queue/ [gyst]
* more styling [gyst]
* style status form [gyst]
* ignore compiled i18n stuff [gyst]
* document mentions todo [gyst]
* strip interpunction from tag index [gyst]
* refactor into re-usable status input provider [gyst]
* protect against site errors on (partial) uninstalls [gyst]
* GS name [gyst]
* implement hashtag filtering [gyst]
* pep8 [gyst]
* version bump to 0.4 [gyst]
* Fix pep8 [avelino]
* add help (tag) in make file [avelino]

0.3 (2012-05-21)
----------------

* update changelog [gyst]
* permission rename s/Read/View/ [gyst]
* use accesscontrols in portlets [gyst]
* disable accesscontrol in lowlevel unittests [gyst]
* add access controls [gyst]
* remove old plone.app.discussion compatibility view [gyst]
* set a default limit to make it hard to accidentally list() a 100k StatusUpdate generator [gyst]
* not using annotations anymore [gyst]
* internal btrees are protected, not private anymore [gyst]
* provide performance-optimized sorting/slicing accessors [gyst]
* remove unused imports [gyst]
* update doc [gyst]
* provide translations [gyst]
* switch from annotationstorage to a utility [gyst]
* clean up interface and method signatures [gyst]
* extract queuing functionality from base class to make life easier for future /self [gyst]
* implement memory queue with batched disk writes for maximal performance [gyst]
* user index accessors [gyst]
* document interface and namespace annotation key [gyst]
* provide test coverage [gyst]
* extract documentation by Maurits on using separate ZODB mount from ploneintranet.activitystream [gyst]
* clean up views, remove plone.app.discussion dependency [gyst]
* refactor view logic WIP [gyst]
* close down some more methods [gyst]
* credit Maurits [gyst]
* refactor storage backend [gyst]
* fork form and viewlet from p.a.d. [gyst]
* Extract Maurits' activity model from ploneintranet.activitystream https://github.com/mauritsvanrees/ploneintranet.activitystream [gyst]
* bump version [gyst]


0.2 (2012-05-04)
----------------

* Prepare ploneintranet.microblog 0.2. [gyst]
* make portlet automatically assignable [gyst]
* async WIP [gyst]
* get rid of src dir indirection [gyst]
* remove unneccessary test [gyst]
* provide "compact" rendering option [gyst]
* remove statuses display, keep only form [gyst]
* fix duplicate commenting bug [gyst]
* unittests [gyst]
* tune doc [gyst]
* update documentation [gyst]
* cleanup [gyst]
* provide proper browserlayer isolation [gyst]
* anchor the microblog portlet to the SiteRoot singleton where we're storing our status updates [gyst]
* customize comment rendering [gyst]
* fork p.a.discussion comments rendering template [gyst]
* render p.a.discussion comments as portlet, not as SiteRoot viewlet [gyst]

0.1 (unreleased)
-------------------

* proof of concept [gyst]
* initial checkin from ZopeSkel [gyst]
