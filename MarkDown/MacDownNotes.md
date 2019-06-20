<link href="../Css/custom.css" rel="stylesheet"></link> 
<div align="center">
<img src="../Resources/Images/Markdown/macdown.png" align="center" width="100"/>
</div>

# MacDown Notes

Some sparse notes about **MacDown**.
You can download the tool for frree at [Macdown Website](http://macdown.uranusjr.com 'Title').
You can find useful setting information here: [Best Markdown Editors for OS X](https://www.raywenderlich.com/119949/top-five-markdown-editors).
You can use also [Visual Studio Code](https://code.visualstudio.com/download) as your markfown editor.

## Custom Styles

Custom styles are not easy to implement across platforms. In the case of Jupyter Notebooks, you can create a **.custom.css** file that is associated with your markdown files. But this is only valid on your machine.
The story is different if you want to apply custom styles on a public platform such Anaconda cloud or GitHub.

On GitHub, for security reasons, you are not allowed to use any css style file remote or otherwise. You cannot even include the style tag.

1.  In a markdown file you can link to a css file, that is stored locally, at the top of the markdown file as follows:
    `<link href="../Css/custom.css" rel="stylesheet"></link>`
1.  In a jupyter notebook file you can link to a css file that is stored locally as follows:

        from IPython.core.display import HTML
        	def set_css_style(css_file_path):
        		styles = open(css_file_path, "r").read()
        		return HTML(styles)

        set_css_style('../Css/custom.css')

<div class="danger">All this does not work in GitHub, this is because GitHub does not allow the style tag for security reasons. </div>

### Style Examples

#### Markers

---

<span class="m_danger">Danger</span>
<span class="m_warning">Warning</span>
<span class="m_success">Success</span>
<span class="m_info">Info</span>
<span class="m_other">Other</span>

#### Notes

---

<div class="danger">Danger</div>
<div class="warning">Warning</div>
<div class="success">Success</div>
<div class="info">Info</div>
<div class="other">Other</div>

## Images

The best way to keep everithing together, is to create an images folder in the same location where you keep your markdown file(s). Then publish the folder along witht the markdown file.
Then you can use the image in the markdown file as follows:
`<img src="../Resources/Images/Markdown/macdown.png" width="400"/>`

The following is the result:

<div align="center">
<img src="../Resources/Images/Markdown/macdown.png" align="center" width="200"/>
</div>

### Remote Reference

You can refer to an image stored in GitHub remotely by using the image raw url format as shown next.

1. From your GitHub repository, get the image URL, as in this example: `https://github.com/milexm/TechnicalNotes/blob/master/Resources/Images/GitHub/git_github_icon.png`
1. Modify the URL to the **raw url format**, as in this example: `https://raw.github.com/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png`.
   Use the above raw URL to refer to the inmage, as in this example:

<img src="https://raw.github.com/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png"/>

For more info, see [github picture path
](https://stackoverflow.com/questions/10935763/github-picture-path).
