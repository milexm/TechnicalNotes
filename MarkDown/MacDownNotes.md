<div align="center">
<img src="../Resources/Images/Markdown/macdown.png" align="center" width="100"/>
</div>

# MacDown Notes
Some sparse notes about **MacDown**. 
You can download the tool for frree at [Macdown Website](http://macdown.uranusjr.com "Title").
You can find useful setting information here: [Best Markdown Editors for OS X](https://www.raywenderlich.com/119949/top-five-markdown-editors). 

## Custom Styles 
Custom styles are not easy to implement across platforms. In the case of Jupyter Notebooks, you can create a **.custom.css** file that is associated with your markdown files. But this is only valid on your machine. 
The story is different if you want to apply custom styles on a public platform such Anaconda cloud or GitHub.

On GitHub, for security reasons, you are not allowed to use any css style file remote or otherwise. The best way is to include the style in the markdown file as you can see next if you edit the file. 

### Style Examples

#### Markers
***
<span class="m_danger">Danger</span> 
<span class="m_warning">Warning</span>
<span class="m_success">Success</span> 
<span class="m_info">Info</span>
<span class="m_other">Other</span>


#### Notes
***
<div class="danger">Danger</div>
<div class="warning">Warning</div>
<div class="success">Success</div>
<div class="info">Info</div>
<div class="other">Other</div>

<style>
/* Custom Markdown styles */

/* Note Red */
.danger {
  background-color: #ffdddd;
  border-left: 6px solid #f44336;
}

/* Note Green */
.success {
  background-color: #ddffdd;
  border-left: 6px solid #4caf50;
}

/* Note Blue */
.info {
  background-color: #e7f3fe;
  border-left: 6px solid #2196f3;
}

/* Note Yellow */
.warning {
  background-color: #ffffcc;
  border-left: 6px solid #ffeb3b;
}

/* Note Gray */
.other {
  background-color: #e7e7e7;
  border-left: 6px solid #696965;
}

/* Marker Yellow */
.m_warning {
  background-color: yellow;
}

/* Marker Gray */
.m_other {
  background-color: lightgray;
}

/* Marker Blue */
.m_info {
  background-color: lightblue;
}

/* Marker Green */
.m_success {
  background-color: #ddffdd;
}

/* Marker Orange */
.m_danger {
  background-color: #ffdddd;
}
</style>


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

1. From your GitHub repository, get the image URL, as in this example: `hhttps://github.com/milexm/TechnicalNotes/blob/master/Resources/Images/GitHub/git_github_icon.png`
1. Modify the URL to the **raw url format**, as in this example: `https://raw.github.com/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png`. 
Use the above raw URL to refer to the inmage, as in this example: 
<img src="https://raw.github.com/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png"/>

A better way to use raw URL, for any file type not only images, is to <span class="m_warning">use the [GitCDN](https://min.gitcdn.link/) service which serves raw files directly from GitHub</span> with proper Content-Type headers and a super fast CDN! 
As in this example: `<img src="https://min.gitcdn.link/repo/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png"/>`

<img src="https://min.gitcdn.link/repo/milexm/TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png"/>

<div class="info">Notice that once you know the URL link for the GitCDN applicable to your repository such as <span class="m_other">https://min.gitcdn.link/repo/milexm/</span> you can just add the path of the file such as <span class="m_other">TechnicalNotes/master/Resources/Images/GitHub/git_github_icon.png</span>.</div>


For more info, see [github picture path
](https://stackoverflow.com/questions/10935763/github-picture-path). 
  