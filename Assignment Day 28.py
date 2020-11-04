#!/usr/bin/env python
# coding: utf-8

# Q1-Create one array of actual values and another array of predicted values. Compare the two sets
# with the confusion matrix.

# In[11]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
y_true = ["honda", "chevrolet", "honda", "toyota", "toyota", "chevrolet"]
y_pred = ["honda", "chevrolet", "honda", "toyota", "toyota", "honda"]
data = confusion_matrix(y_true, y_pred)
sns.heatmap(data,cmap='Blues',annot=True)


# In[6]:


#Q2
tn=42
tp=32
fn=18
fp=8
accuracy=(tp+tn)/(tp+tn+fn+fp)
precision=tp/(tp+fp)
recall=tp/(tp+fn)
print("Accuracy: ",accuracy)
print("Precision: ",precision)
print("Recall: ",recall)


# In[ ]:




