Title: Test Post One
Date: 2014-07-28 11:09
Modified: 2014-07-28 11:09
Category: Test
Tags: pelican, Test
Slug: my-test-post-1
Authors: Shouren 

Welcome to StackEdit!
===================


Hello, I'm your first Markdown document in **StackEdit**[^stackedit]. Don't delete me, I can be helpful. I can be recovered anyway in the **Utils** tab of the <i class="icon-cog"></i> **Settings** dialog.

----------


Documents
-------------

**StackEdit** stores your documents in your browser, which means all your documents are automatically saved locally and are accessible **offline!**

> **Note:**

> - StackEdit is accessible offline after the application has been loaded for the first time.
> - Your local documents are not shared between different browsers or computers.
> - Clearing your browser's data may **delete all your local documents!** Make sure your documents are synchronized with your **Google Drive** or your **Dropbox** account (check out the [<i class="icon-refresh"></i> Synchronization](#synchronization) section).

#### <i class="icon-file"></i> Create a document

The document panel is accessible using  <i class="icon-folder-open"></i> button in the navigation bar. You can create a new document by clicking <i class="icon-file"></i> **New document** in the document panel.

#### <i class="icon-folder-open"></i> Switch to another document

All your local documents are listed in the document panel. You can switch from one to another by clicking a document in the list or you can toggle documents using <kbd>Ctrl+[</kbd> and <kbd>Ctrl+]</kbd>.

#### <i class="icon-pencil"></i> Rename a document

You can rename the current document by clicking the document title in the navigation bar.

#### <i class="icon-trash"></i> Delete a document

You can delete the current document by clicking <i class="icon-trash"></i> **Delete document** in the document panel.

#### <i class="icon-hdd"></i> Export a document

You can save the current document to a file by clicking <i class="icon-hdd"></i> **Export to disk** from the <i class="icon-provider-stackedit"></i> menu panel.

> **Tip:** Check out the [<i class="icon-upload"></i> Publish a document](#publish-a-document) section for a description of the different output formats.


----------


Synchronization
-------------------

**StackEdit** can be combined with <i class="icon-provider-gdrive"></i> **Google Drive** and <i class="icon-provider-dropbox"></i> **Dropbox** to have your documents centralized in the *Cloud*. The synchronization mechanism will take care of uploading your modifications or downloading the latest version of your documents.

> **Note:**

> - Full access to **Google Drive** or **Dropbox** is required to be able to import any document in StackEdit. Permission restrictions can be configured in the settings.
> - Imported documents are downloaded in your browser and are not transmitted to a server.
> - If you experience problems saving your documents on Google Drive, check and optionally disable browser extensions, such as Disconnect.

#### <i class="icon-refresh"></i> Open a document

You can open a document from <i class="icon-provider-gdrive"></i> **Google Drive** or the <i class="icon-provider-dropbox"></i> **Dropbox** by opening the <i class="icon-refresh"></i> **Synchronize** sub-menu and by clicking **Open from...**. Once opened, any modification in your document will be automatically synchronized with the file in your **Google Drive** / **Dropbox** account.

#### <i class="icon-refresh"></i> Save a document

You can save any document by opening the <i class="icon-refresh"></i> **Synchronize** sub-menu and by clicking **Save on...**. Even if your document is already synchronized with **Google Drive** or **Dropbox**, you can export it to a another location. **StackEdit** can synchronize one document with multiple locations and accounts.

#### <i class="icon-refresh"></i> Synchronize a document

Once your document is linked to a <i class="icon-provider-gdrive"></i> **Google Drive** or a <i class="icon-provider-dropbox"></i> **Dropbox** file, **StackEdit** will periodically (every 3 minutes) synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be detected.

If you just have modified your document and you want to force the synchronization, click the <i class="icon-refresh"></i> button in the navigation bar.

> **Note:** The <i class="icon-refresh"></i> button is disabled when you have no document to synchronize.

#### <i class="icon-refresh"></i> Manage document synchronization

Since one document can be synchronized with multiple locations, you can list and manage synchronized locations by clicking <i class="icon-refresh"></i> **Manage synchronization** in the <i class="icon-refresh"></i> **Synchronize** sub-menu. This will let you remove synchronization locations that are associated to your document.

> **Note:** If you delete the file from **Google Drive** or from **Dropbox**, the document will no longer be synchronized with that location.

----------


Publication
-------------

Once you are happy with your document, you can publish it on different websites directly from **StackEdit**. As for now, **StackEdit** can publish on **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **Tumblr**, **WordPress** and on any SSH server.

#### <i class="icon-upload"></i> Publish a document

You can publish your document by opening the <i class="icon-upload"></i> **Publish** sub-menu and by choosing a website. In the dialog box, you can choose the publication format:

- Markdown, to publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML, to publish the document converted into HTML (on a blog for example),
- Template, to have a full control of the output.

> **Note:** The default template is a simple webpage wrapping your document in HTML format. You can customize it in the **Advanced** tab of the <i class="icon-cog"></i> **Settings** dialog.

#### <i class="icon-upload"></i> Update a publication

After publishing, **StackEdit** will keep your document linked to that publication which makes it easy for you to update it. Once you have modified your document and you want to update your publication, click on the <i class="icon-upload"></i> button in the navigation bar.

> **Note:** The <i class="icon-upload"></i> button is disabled when your document has not been published yet.

#### <i class="icon-upload"></i> Manage document publication

Since one document can be published on multiple locations, you can list and manage publish locations by clicking <i class="icon-upload"></i> **Manage publication** in the <i class="icon-provider-stackedit"></i> menu panel. This will let you remove publication locations that are associated to your document.

> **Note:** If the file has been removed from the website or the blog, the document will no longer be published on that location.

----------


Markdown Extra
--------------------

**StackEdit** supports **Markdown Extra**, which extends **Markdown** syntax with some nice features.

> **Tip:** You can disable any **Markdown Extra** feature in the **Extensions** tab of the <i class="icon-cog"></i> **Settings** dialog.

> **Note:** You can find more information about **Markdown** syntax [here][2] and **Markdown Extra** extension [here][3].


### Tables

**Markdown Extra** has a special syntax for tables:

Item     | Value
-------- | ---
Computer | $1600
Phone    | $12
Pipe     | $1

You can specify column alignment with one or two colons:

| Item     | Value | Qty   |
| :------- | ----: | :---: |
| Computer | $1600 |  5    |
| Phone    | $12   |  12   |
| Pipe     | $1    |  234  |


### Definition Lists

**Markdown Extra** has a special syntax for definition lists too:

Term 1
Term 2
:   Definition A
:   Definition B

Term 3

:   Definition C

:   Definition D

    > part of definition D


### Fenced code blocks

GitHub's fenced code blocks[^gfm] are also supported with **Prettify** syntax highlighting:

```
// Foo
var bar = 0;
```

> **Tip:** To use **Highlight.js** instead of **Prettify**, just configure the **Markdown Extra** extension in the <i class="icon-cog"></i> **Settings** dialog.

> **Note:** You can find more information:

> - about **Prettify** syntax highlighting [here][5],
> - about **Highlight.js** syntax highlighting [here][6].


### Footnotes

You can create footnotes like this[^footnote].

  [^footnote]: Here is the *text* of the **footnote**.


### SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                  | ASCII                        | HTML              |
 ----------------- | ---------------------------- | ------------------
| Single backticks | `'Isn't this fun?'`            | 'Isn't this fun?' |
| Quotes           | `"Isn't this fun?"`            | "Isn't this fun?" |
| Dashes           | `-- is en-dash, --- is em-dash` | -- is en-dash, --- is em-dash |


### Table of contents

You can insert a table of contents using the marker `[TOC]`:

[TOC]


### MathJax

You can render *LaTeX* mathematical expressions using **MathJax**, as on [math.stackexchange.com][1]:

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> **Tip:** Make sure you include **MathJax** into your publications to render mathematical expression properly. Your page/template should include something like this:

```
<script type="text/javascript" src="https://stackedit.io/libs/MathJax/MathJax.js?config=TeX-AMS_HTML"></script>
```

> **Note:** You can find more information about **LaTeX** mathematical expressions [here][4].


### UML diagrams

You can also render sequence diagrams like this:

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

<svg style="overflow: hidden; position: relative; top: -0.683105px;" xmlns="http://www.w3.org/2000/svg" width="381.3500089645386" version="1.1" height="270"><desc>Created with Raphaël 2.1.0</desc><defs><path id="raphael-marker-block" d="M5,0 0,2.5 5,5z" stroke-linecap="round"></path><marker refY="2.5" refX="2.5" orient="auto" markerWidth="5" markerHeight="5" id="raphael-marker-endblock55"><use stroke="none" fill="#000" stroke-width="1.0000" transform="rotate(180 2.5 2.5) scale(1,1)" xlink:href="#raphael-marker-block"></use></marker></defs><rect stroke-width="2" style="" stroke="#000000" fill="none" ry="0" rx="0" r="0" height="40" width="51.63333320617676" y="20" x="10"></rect><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="31.633333206176758" y="30" x="19.999998092651367"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="40" x="35.81666660308838" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Alice</tspan></text><rect stroke-width="2" style="" stroke="#000000" fill="none" ry="0" rx="0" r="0" height="40" width="51.63333320617676" y="210" x="10"></rect><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="31.633333206176758" y="220" x="19.999998092651367"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="230" x="35.81666660308838" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Alice</tspan></text><path stroke-width="2" d="M35.81666660308838,60L35.81666660308838,210" stroke="#000000" fill="none" style=""></path><rect stroke-width="2" style="" stroke="#000000" fill="none" ry="0" rx="0" r="0" height="40" width="47.266666412353516" y="20" x="184.96667385101318"></rect><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="27.266666412353516" y="30" x="194.9666748046875"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="40" x="208.60000705718994" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Bob</tspan></text><rect stroke-width="2" style="" stroke="#000000" fill="none" ry="0" rx="0" r="0" height="40" width="47.266666412353516" y="210" x="184.96667385101318"></rect><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="27.266666412353516" y="220" x="194.9666748046875"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="230" x="208.60000705718994" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Bob</tspan></text><path stroke-width="2" d="M208.60000705718994,60L208.60000705718994,210" stroke="#000000" fill="none" style=""></path><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="152.78334045410156" y="75" x="45.81666946411133"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="85" x="122.20833683013916" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Hello Bob, how are you?</tspan></text><path stroke-dasharray="0" marker-end="url(#raphael-marker-endblock55)" stroke-width="2" d="M35.81666660308838,100C35.81666660308838,100,175.20985300321718,100,203.5921570700403,100" stroke="#000000" fill="none" style=""></path><rect stroke-width="2" style="" stroke="#000000" fill="none" ry="0" rx="0" r="0" height="30" width="79.11666870117188" y="120" x="228.60000705718994"></rect><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="69.11666870117188" y="125" x="233.6000213623047"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="135" x="268.1583414077759" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">Bob thinks</tspan></text><rect style="" stroke="none" fill="#ffffff" ry="0" rx="0" r="0" height="20" width="114.25" y="165" x="65.08333587646484"></rect><text font-family="sans-serif" font-size="16px" fill="#000000" stroke="none" font="10px &quot;Arial&quot;" text-anchor="middle" y="175" x="122.20833683013916" style="text-anchor: middle; font: 16px sans-serif;"><tspan dy="5">I am good thanks!</tspan></text><path stroke-dasharray="6,2" marker-end="url(#raphael-marker-endblock55)" stroke-width="2" d="M208.60000705718994,190C208.60000705718994,190,69.20682065706114,190,40.82451659023805,190" stroke="#000000" fill="none" style=""></path></svg>

And flow charts like this:

```flow
st=>start: Start
e=>end
op=>operation: My Operation
cond=>condition: Yes or No?

st->op->cond
cond(yes)->e
cond(no)->op
```

> **Note:** You can find more information:

> - about **Sequence diagrams** syntax [here][7],
> - about **Flow charts** syntax [here][8].

  [^stackedit]: [StackEdit](https://stackedit.io/) is a full-featured, open-source Markdown editor based on PageDown, the Markdown library used by Stack Overflow and the other Stack Exchange sites.

  [^gfm]: **GitHub Flavored Markdown** (GFM) is supported in StackEdit.


  [1]: http://math.stackexchange.com/
  [2]: http://daringfireball.net/projects/markdown/syntax "Markdown"
  [3]: https://github.com/jmcmanus/pagedown-extra "Pagedown Extra"
  [4]: http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
  [5]: https://code.google.com/p/google-code-prettify/
  [6]: http://highlightjs.org/
  [7]: http://bramp.github.io/js-sequence-diagrams/
  [8]: http://adrai.github.io/flowchart.js/


